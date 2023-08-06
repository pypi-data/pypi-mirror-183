"""Module defining the node and base estimator classes for a decision tree."""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from typing import Optional

import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype


@dataclass(kw_only=True)
class Node:
    """A Decision Tree Node

    Parameters
    ----------
    data
        - the dataset resulting from a split of the parent node on a feature value.

    feature
        - the descriptive or target feature value of a node.

    threshold ([0-9]*)
        - the feature value to partition the dataset into two levels with some range.

    branch (< | >= [0-9]*)
        - the feature value on a split from the parent node on a feature value.

    parent
        - the precedent node along the path from the root to a node.

    depth
        - the number of levels from the root to a node.

    children
        - the nodes on each split of the parent node for each unique feature values.
    """

    data: Optional[pd.DataFrame.dtypes]
    feature: str
    threshold: Optional[float] = None
    branch: Optional[str]
    parent: Optional[Node] = None
    depth: int
    children: dict = field(default_factory=dict)

    def __str__(self):
        if self.threshold:
            return (
                self.depth * "\t" + f"{self.feature} ({list(self.children.keys())[0]})"
            )
        if self.is_leaf and self.parent and self.parent.threshold:
            return self.depth * "\t" + f"{self.feature}"

        return self.depth * "\t" + f"{self.feature} ({self.branch})"

    def __eq__(self, other):
        """Checks if two nodes are identical."""
        if not isinstance(self, type(other)):
            raise TypeError("Object is not a 'Node' instance")

        return (
            self.feature == other.feature
            and self.threshold == other.threshold
            and self.branch == other.branch
            and self.parent == other.parent
            and self.depth == other.depth
        )

    def add_child(self, node: Node):
        """Adds another node to the node's children."""
        self.children[node.branch] = node

    @property
    def is_leaf(self):
        """Returns whether a node is terminal."""
        return not self.children

    @property
    def X(self):
        """Returns the feature matrix of a node."""
        return self.data[0]

    @property
    def y(self):
        """Returns the target vector of a node."""
        return self.data[1]

    @property
    def left(self):
        """Returns the left child of a node."""
        return self.children.get(f"< {self.threshold}")

    @property
    def right(self):
        """Returns the right child of a node."""
        return self.children.get(f">= {self.threshold}")


class DecisionTreeEstimator:
    """A Decision Tree Estimator"""

    def __init__(self, *, metric=None, criterion=None):
        """
        Parameters
        ----------
        root
            - the starting node with depth zero of a decision tree.

        n_levels
            - contains a list of all unique feature values for each descriptive feature.

        n_thresholds
            - contains the possible splits of the continuous feature being tested.

        metric
            - a measure of impurity.

        criterion (pre-pruning)
            - {max_depth, partition_threshold, low_gain}.
        """

        self.root = None
        self._n_levels = None
        self._n_thresholds = {}

        self._metric = metric
        self._criterion = criterion

    def __iter__(self, node=None):
        if not node:
            node = self.root

        yield node

        for child in node.children.values():
            yield from self.__iter__(child)

    def __str__(self):
        """Pre-order traversal a decision tree."""
        if not self._check_is_fitted:
            raise AttributeError("Decision tree is not fitted")

        return "\n".join(map(str, self))

    def __eq__(self, other: DecisionTreeEstimator):
        """Checks if two decision trees are identical."""
        if not isinstance(self, type(other)):
            raise TypeError("Object is not a 'DecisionTreeEstimator' instance")
        if not (self._check_is_fitted and other._check_is_fitted):
            raise AttributeError("At least one 'DecisionTreeEstimator' is not fitted")

        return all(lhs == rhs for lhs, rhs in zip(self, other))

    @property
    def _check_is_fitted(self):
        """Checks whether a decision tree is fitted."""
        return bool(self.root)

    def _find_optimal_threshold(self, X, y, d):
        """Computes the optimal threshold between different target levels instances."""
        df = pd.concat([X, y], axis=1)
        df.sort_values(by=[d], inplace=True)

        thresholds = []
        for i in range(len(df) - 1):
            pairs = df.iloc[i : i + 2, -1]
            if any(pairs.iloc[0] != val for val in pairs.values):
                thresholds.append(df.loc[pairs.index, d].mean())

        levels = []
        for threshold in thresholds:
            left, right = df.loc[df[d] < threshold], df.loc[df[d] >= threshold]

            weight_left = len(left.loc[left[d] < threshold]) / len(df)
            weight_right = len(right.loc[right[d] >= threshold]) / len(df)

            metric = self._metric(df.iloc[:, :-1], df.iloc[:, -1])
            metric_left = self._metric(left.iloc[:, :-1], left.iloc[:, -1])
            metric_right = self._metric(right.iloc[:, :-1], right.iloc[:, -1])

            rem = metric_left * weight_left + metric_right * weight_right

            levels.append(metric - rem)

        return max(levels), thresholds[np.argmax(levels)], rem

    def _partition_data(self, X, y, d, t):
        """Returns a subset of the training data with feature (d) and level (t)."""
        df = pd.concat([X.loc[X[d] == t], y.loc[X[d] == t]], axis=1)
        df = df.drop([d], axis=1)
        return df.iloc[:, :-1], df.iloc[:, -1], t

    def fit(self, X, y):
        """Fits a decision tree estimator."""
        if X.empty or y.empty:
            raise Exception("Dataset is empty")

        self._n_levels = {d: X[d].unique() for d in X.columns}

    def predict(self, x, node=None):
        """Predicts a test sample on a decision tree."""
        if not node:
            node = self.root
        if node.is_leaf:
            return node

        query_branch = x[node.feature].values[0]

        if is_numeric_dtype(query_branch):
            next_node = node.left if query_branch < node.threshold else node.right
        else:
            try:
                next_node = node.children[query_branch]
            except KeyError:
                sys.exit(f"Branch {node.feature} -> {query_branch} does not exist")

        return self.predict(x, next_node)
