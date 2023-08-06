"""Module containing the parallel decision tree classifier implementation."""


from copy import deepcopy
from statistics import mode

import numpy as np
from mpi4py import MPI
from pandas.api.types import is_numeric_dtype
from sklearn.metrics import accuracy_score

from .base_estimator import DecisionTreeEstimator, Node

world_comm = MPI.COMM_WORLD
world_rank = world_comm.Get_rank()
world_size = world_comm.Get_size()


class ParallelDecisionTreeClassifier(DecisionTreeEstimator):
    """A Rudimentary Parallel Decision Tree Classifier"""

    def __init__(self, *, criterion=None):
        super().__init__(metric=self._find_entropy, criterion=criterion)

    def _find_entropy(self, X, y):
        """Measures the amount of impurity in (X, y)."""

        def proba(t):
            return len(X.loc[y == t]) / len(X)

        return -np.sum([proba(t) * np.log2(proba(t)) for t in np.unique(y)])

    def _find_rem(self, X, y, d):
        """Measures the entropy after testing feature (d)."""

        def weight(t):
            return len(X.loc[X[d] == t]) / len(X)

        return np.sum(
            [
                weight(t) * self._metric(X.loc[X[d] == t], y.loc[X[d] == t])
                for t in np.unique(X[d])
            ]
        )

    def _find_information_gain(self, X, y, d):
        """Measures the reduction in the overall entropy by testing on feature."""
        if is_numeric_dtype(X[d]):
            gain, optimal_threshold, _ = super()._find_optimal_threshold(X, y, d)
            self._n_thresholds[d] = optimal_threshold
            return gain

        gain = self._metric(X, y) - self._find_rem(X, y, d)
        return gain

    def fit(self, X, y):
        """Fits the decision tree classifier to the dataset."""
        super().fit(X, y)
        self.root = self.make_tree(X, y)
        return self

    def make_tree(self, X, y, *, comm=world_comm, parent=None, branch=None, depth=0):
        """Performs the ID3 algorithm.

        Base Cases
        ----------
        - All instances have the same labels.
        - Dataset is empty.
        - If all feature values are identical.
        - Max depth reached.
        - Max number of instances in partitioned dataset reached.
        """

        def make_node(feature):
            return Node(
                data=(X, y),
                feature=feature,
                branch=branch,
                parent=parent,
                depth=depth,
            )

        rank = comm.Get_rank()
        size = comm.Get_size()

        if len(np.unique(y)) == 1:
            return make_node(y.iat[0])
        if X.empty:
            return make_node(mode(parent.y))
        if all((X[d] == X[d].iloc[0]).all() for d in X.columns):
            return make_node(mode(y))
        if self._criterion.get("max_depth", float("inf")) <= depth:
            return make_node(mode(y))
        if self._criterion.get("partition_threshold", float("-inf")) >= len(X):
            return make_node(mode(y))

        # def prange(X, rank, size):
        #     i = len(X.columns) // size
        #     j = len(X.columns) % size
        #     start = rank * i + min(rank, j)
        #     end = start + i - int(rank >= j) + 1
        #     return X.columns[start:end]

        max_gain = np.argmax([self._find_information_gain(X, y, d) for d in X.columns])

        # gain = comm.allgather(
        #     [self._find_information_gain(X, y, d) for d in prange(X, rank, size)]
        # )
        # max_gain = np.argmax(np.ravel(gain))

        if self._criterion.get("low_gain", float("-inf")) >= max_gain:
            return make_node(mode(y))

        best_feature = X.columns[max_gain]
        best_node = deepcopy(make_node(best_feature))

        if is_numeric_dtype(X[best_feature]):
            # self._n_thresholds |= comm.bcast(round(self._n_thresholds, 2))
            best_node.threshold = round(self._n_thresholds[best_feature], 2)
            left = [
                X.loc[X[best_feature] < best_node.threshold],
                y.loc[X[best_feature] < best_node.threshold],
                f"< {best_node.threshold}",
            ]
            right = [
                X.loc[X[best_feature] >= best_node.threshold],
                y.loc[X[best_feature] >= best_node.threshold],
                f">= {best_node.threshold}",
            ]
            levels = [left, right]
        else:
            levels = [
                self._partition_data(X, y, best_feature, level)
                for level in self._n_levels[best_feature]
            ]

        if size == 1:
            for *d, level in levels:
                best_node.add_child(
                    self.make_tree(
                        *d, comm=comm, parent=best_node, branch=level, depth=depth + 1
                    )
                )
        else:
            ratio = size // len(levels)
            color = rank // ratio % len(levels)
            key = rank % ratio + ratio * (rank >= ratio * len(levels))

            group = comm.Split(color, key)
            *d, level = levels[color]

            sub_tree = comm.allgather(
                {
                    level: self.make_tree(
                        *d, comm=group, parent=best_node, branch=level, depth=depth + 1
                    )
                }
            )

            best_node.children |= {k: v for d in sub_tree for k, v in d.items()}

            group.Free()

        return best_node

    def score(self, X, y):
        """Evaluates the decision tree model on the test set."""
        y_hat = [self.predict(X.iloc[x].to_frame().T).feature for x in range(len(X))]
        return accuracy_score(y, y_hat)
