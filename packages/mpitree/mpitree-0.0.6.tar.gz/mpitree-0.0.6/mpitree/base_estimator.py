"""Module defining the node and base estimator classes for a decision tree."""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from itertools import starmap
from operator import eq
from typing import Optional

import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype


@dataclass(kw_only=True)
class Node:
    """A Decision Tree Node

    Parameters
    ----------
    data : optional pd.DataFrame.dtypes, default=None
        - the dataset resulting from a split of the parent node on a feature value.

    feature : str, default=""
        - the descriptive or target feature value of a node.

    threshold : optional int, default=None
        - the feature value to partition the dataset into two levels with some range.

    branch : optional str, default=None
        - the feature value on a split from the parent node on a feature value.

    parent : optional Node, default=None
        - the precedent node along the path from the root to a node.

    depth : int, default=0
        - the number of levels from the root to a node.

    children : dict[Node], default=dict
        - the nodes on each split of the parent node for each unique feature values.
    """

    data: Optional[pd.DataFrame.dtypes] = None
    feature: str = ""
    threshold: Optional[float] = None
    branch: Optional[str] = None
    parent: Optional[Node] = None
    depth: int = 0
    children: dict = field(default_factory=dict)

    def __str__(self):
        """Displays the nodes properties

        >>> str(Node())
        ' (None)'
        >>> str(Node(feature="Alice", branch="branch", depth=1))
        '\\tAlice (branch)'
        >>> str(Node(feature="Bob", threshold=0.0, depth=1, children={"< 0": Node()}))
        '\\tBob (< 0)'
        >>> str(Node(feature="John", branch="branch", parent=Node(threshold=0.0)))
        'John'
        """
        if self.threshold is not None:
            return (
                self.depth * "\t" + f"{self.feature} ({list(self.children.keys())[0]})"
            )
        if self.is_leaf and self.parent and self.parent.threshold is not None:
            return self.depth * "\t" + f"{self.feature}"

        return self.depth * "\t" + f"{self.feature} ({self.branch})"

    def __eq__(self, other):
        """Checks if two nodes are identical

        >>> Node() == "Not a Node"
        Traceback (most recent call last):
            ...
        TypeError: Object is not a `Node` instance
        >>> Node() == Node()
        True
        >>> Node(feature="Alice") == Node(feature="Bob")
        False
        """
        if not isinstance(self, type(other)):
            raise TypeError("Object is not a `Node` instance")

        return (
            self.feature == other.feature
            and self.threshold == other.threshold
            and self.branch == other.branch
            and self.parent == other.parent
            and self.depth == other.depth
        )

    def __add__(self, other):
        """Adds another node to the node's children

        >>> Node() + "Not a Node"
        Traceback (most recent call last):
            ...
        TypeError: Object is not a `Node` instance
        >>> (Node() + Node(branch="< 0")).is_leaf
        False
        """
        if not isinstance(self, type(other)):
            raise TypeError("Object is not a `Node` instance")
        self.children[other.branch] = other
        return self

    @property
    def is_leaf(self):
        """Returns whether a node is terminal

        >>> Node().is_leaf
        True
        >>> Node(children={"branch": Node()}).is_leaf
        False
        """
        return not self.children

    @property
    def X(self):
        """Returns the feature matrix of a node

        >>> Node(data=(pd.DataFrame({"X": [0, 1]}), pd.DataFrame({"y": [0, 1]}))).X
           X
        0  0
        1  1
        >>> Node(data=(pd.DataFrame({"X": []}), pd.DataFrame({"y": []}))).X.empty
        True
        """
        return self.data[0]

    @property
    def y(self):
        """Returns the target vector of a node

        >>> Node(data=(pd.DataFrame({"X": [0, 1]}), pd.DataFrame({"y": [0, 1]}))).y
           y
        0  0
        1  1
        >>> Node(data=(pd.DataFrame({"X": []}), pd.DataFrame({"y": []}))).y.empty
        True
        """
        return self.data[1]

    @property
    def left(self):
        """Returns the left child of a node

        >>> print(Node().left)
        None
        >>> print(Node(threshold=0, children={"< 0": 0}).left)
        0
        """
        return self.children.get(f"< {self.threshold}")

    @property
    def right(self):
        """Returns the right child of a node

        >>> print(Node().right)
        None
        >>> print(Node(threshold=0, children={">= 0": 0}).right)
        0
        """
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
            - {max_depth, min_samples_split, min_gain}.
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

        return all(starmap(eq, zip(self, other)))

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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
