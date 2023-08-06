#!/usr/bin/env python3

import sys

sys.path.append("..")

import unittest

import pandas as pd
from pandas.testing import assert_frame_equal, assert_series_equal

from mpitree.base_estimator import Node


class TestNode(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({"X": [0, 1, 2], "y": [0, 1, 2]})
        self.X, self.y = self.data.iloc[:, :-1], self.data.iloc[:, -1]

        self.A = Node(data=None, feature="A", branch="0", parent=None, depth=0)
        self.B = Node(
            data=(self.X, self.y),
            feature="",
            threshold=0,
            branch=None,
            parent=None,
            depth=1,
            children={"< 0": 0, ">= 0": 0},
        )

    def test_node_str(self):
        self.assertEqual(str(self.A), "A (0)")
        self.assertEqual(str(self.B), "\t (None)")

    def test_node_eq(self):
        with self.assertRaises(TypeError):
            self.A == "Not a Node"

        self.assertTrue(self.A == self.A, "Expected node A to be equal to node A")
        self.assertFalse(
            self.A == self.B, "Expected node A to be different from node B"
        )

    def test_node_is_leaf(self):
        self.assertTrue(self.A.is_leaf, "Expected node A to be a leaf node")
        self.assertFalse(self.B.is_leaf, "Expected node B to not be a leaf node")

    def test_node_left_and_right(self):
        self.assertIsNone(self.A.left, "Expected node A to have no left child")
        self.assertIsNone(self.A.right, "Expected node A to have no right child")
        self.assertIsNotNone(self.B.left, "Expected node B to have a left child")
        self.assertIsNotNone(self.B.right, "Expected node B to have a right child")

    def test_node_X_and_y(self):
        assert_frame_equal(self.B.X, self.X)
        assert_series_equal(self.B.y, self.y)


if __name__ == "__main__":
    unittest.main(verbosity=2)
