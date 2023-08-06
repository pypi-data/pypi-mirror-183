#!/usr/bin/env python3

import sys

sys.path.append("..")

import unittest

import pandas as pd

from src.mpitree.decision_tree import DecisionTreeClassifier, DecisionTreeRegressor


def generate_data(features: dict) -> tuple:
    data = pd.DataFrame(features)
    return data.iloc[:, :-1], data.iloc[:, -1]


class TestDecisionTreeEstimator(unittest.TestCase):
    def test_make_tree_with_empty_dataset(self):
        with self.assertRaises(Exception):
            DecisionTreeClassifier(criterion={}).fit(*generate_data({"A": [], "y": []}))

    def test_eq(self):
        X, y = generate_data({"A": ["a"], "y": ["+"]})
        tree_a = DecisionTreeClassifier(criterion={}).fit(X, y)
        X, y = generate_data({"A": ["a"], "y": ["-"]})
        tree_b = DecisionTreeClassifier(criterion={}).fit(X, y)

        with self.assertRaises(TypeError):
            tree_a == "Not a Decision Tree"

        with self.assertRaises(AttributeError):
            tree_a == DecisionTreeClassifier(criterion={})
            DecisionTreeClassifier(criterion={}) == tree_a

        self.assertTrue(tree_a == tree_a)
        self.assertFalse(tree_a == tree_b)

    def test_str_with_tree_not_fitted(self):
        with self.assertRaises(AttributeError):
            str(DecisionTreeClassifier(criterion={}))

    def test_check_is_fitted(self):
        X, y = generate_data({"A": ["a"], "y": ["+"]})
        self.assertTrue(DecisionTreeClassifier(criterion={}).fit(X, y)._check_is_fitted)
        self.assertFalse(DecisionTreeClassifier(criterion={})._check_is_fitted)

    def test_max_depth(self):
        X, y = generate_data({"A": [1, 2, 3, 4], "B": [7, 8, 5, 6], "y": [1, 2, 1, 2]})
        tree = DecisionTreeClassifier(criterion={"max_depth": 1}).fit(X, y)
        self.assertTrue(max(node.depth for node in tree) == 1)


class TestDecisionTreeClassifier(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame(
            {
                "A": ["0", "0", "1", "1"],
                "B": ["1", "1", "0", "0"],
                "y": ["0", "1", "0", "1"],
            }
        )
        self.X, self.y = self.data.iloc[:, :-1], self.data.iloc[:, -1]

    def test_find_optimal_threshold(self):
        X, y = generate_data({"A": [0, 1, 2, 3], "y": ["0", "1", "0", "1"]})
        self.assertEqual(
            DecisionTreeClassifier(criterion={})._find_optimal_threshold(X, y, "A")[1],
            0.5,
        )

        X, y = generate_data({"A": [0, 0, 1, 3], "y": ["0", "0", "0", "1"]})
        self.assertEqual(
            DecisionTreeClassifier(criterion={})._find_optimal_threshold(X, y, "A")[1],
            2,
        )

    def test_find_entropy(self):
        self.assertEqual(
            DecisionTreeClassifier(criterion={})._find_entropy(self.X, self.y), 1
        )

    def test_find_rem(self):
        self.assertEqual(
            DecisionTreeClassifier(criterion={})._find_rem(self.X, self.y, "A"), 1
        )

    def test_find_information_gain(self):
        self.assertEqual(
            DecisionTreeClassifier(criterion={})._find_information_gain(
                self.X, self.y, "A"
            ),
            0,
        )

    def test_make_tree_with_categorical_variables(self):
        X, y = generate_data({"A": ["a"], "y": ["+"]})
        self.assertEqual(
            str(DecisionTreeClassifier(criterion={}).fit(X, y)), "+ (None)"
        )

        X, y = generate_data(
            {"A": ["a", "a", "a"], "B": ["a", "a", "a"], "y": ["+", "+", "-"]}
        )
        self.assertEqual(
            str(DecisionTreeClassifier(criterion={}).fit(X, y)), "+ (None)"
        )

        X, y = generate_data(
            {
                "A": ["a", "a", "b", "b"],
                "B": ["a", "b", "a", "b"],
                "y": ["+", "-", "+", "-"],
            }
        )
        self.assertEqual(
            str(DecisionTreeClassifier(criterion={}).fit(X, y)),
            "B (None)\n\t+ (a)\n\t- (b)",
        )

    def test_make_tree_with_continuous_variables(self):
        X, y = generate_data({"A": [1], "y": ["+"]})
        self.assertEqual(
            str(DecisionTreeClassifier(criterion={}).fit(X, y)), "+ (None)"
        )

        X, y = generate_data({"A": [1, 1, 1], "B": [1, 1, 1], "y": ["+", "+", "-"]})
        self.assertEqual(
            str(DecisionTreeClassifier(criterion={}).fit(X, y)), "+ (None)"
        )

        X, y = generate_data(
            {"A": [1, 2, 3, 4], "B": [7, 8, 5, 6], "y": ["+", "+", "+", "-"]}
        )
        self.assertEqual(
            str(DecisionTreeClassifier(criterion={}).fit(X, y)),
            "A (< 3.5)\n\t+\n\t-",
        )

    def test_make_tree_with_categorical_and_continuous_variables(self):
        X, y = generate_data({"A": ["a"], "B": [1], "y": ["+"]})
        self.assertEqual(
            str(DecisionTreeClassifier(criterion={}).fit(X, y)), "+ (None)"
        )

        X, y = generate_data(
            {"A": ["a", "a", "a"], "B": [1, 1, 1], "y": ["+", "+", "-"]}
        )
        self.assertEqual(
            str(DecisionTreeClassifier(criterion={}).fit(X, y)), "+ (None)"
        )

        X, y = generate_data({"A": ["a", "a"], "B": [3, 1], "y": ["-", "+"]})
        self.assertEqual(
            str(DecisionTreeClassifier(criterion={}).fit(X, y)),
            "B (< 2.0)\n\t+\n\t-",
        )


class TestDecisionTreeRegressor(unittest.TestCase):
    def test_find_variance(self):
        X, y = generate_data({"A": ["0"], "y": [0]})
        self.assertEqual(DecisionTreeRegressor(criterion={})._find_variance(X, y), 0)

        X, y = generate_data({"A": ["0", "0"], "y": [0, 1]})
        self.assertEqual(DecisionTreeRegressor(criterion={})._find_variance(X, y), 0.5)

    def test_find_weighted_variance(self):
        X, y = generate_data({"A": ["0", "0", "1", "1"], "y": [0, 1, 0, 1]})
        self.assertEqual(
            DecisionTreeRegressor(criterion={})._find_weighted_variance(X, y, "A"), 0.5
        )

    def test_make_tree_with_categorical_variables(self):
        X, y = generate_data({"A": ["a"], "y": [1]})
        self.assertEqual(str(DecisionTreeRegressor(criterion={}).fit(X, y)), "1 (None)")

        X, y = generate_data(
            {"A": ["a", "a", "a"], "B": ["a", "a", "a"], "y": [2, 2, 2]}
        )
        self.assertEqual(str(DecisionTreeRegressor(criterion={}).fit(X, y)), "2 (None)")

        X, y = generate_data(
            {"A": ["a", "a", "b", "b"], "B": ["a", "b", "a", "b"], "y": [1, 2, 1, 2]}
        )
        self.assertEqual(
            str(DecisionTreeRegressor(criterion={}).fit(X, y)),
            "B (None)\n\t1 (a)\n\t2 (b)",
        )

    def test_make_tree_with_continuous_variables(self):
        X, y = generate_data({"A": [1], "y": [1]})
        self.assertEqual(str(DecisionTreeRegressor(criterion={}).fit(X, y)), "1 (None)")

        X, y = generate_data({"A": [1, 1, 1], "B": [1, 1, 1], "y": [2, 2, 2]})
        self.assertEqual(str(DecisionTreeRegressor(criterion={}).fit(X, y)), "2 (None)")

        X, y = generate_data({"A": [1, 2, 3, 4], "B": [7, 8, 5, 6], "y": [1, 2, 1, 2]})
        self.assertEqual(
            str(DecisionTreeRegressor(criterion={}).fit(X, y)),
            "A (< 1.5)\n\t1\n\tA (< 2.5)\n\t\t2\n\t\tA (< 3.5)\n\t\t\t1\n\t\t\t2",
        )

    def test_make_tree_with_categorical_and_continuous_variables(self):
        X, y = generate_data({"A": ["a"], "B": [1], "y": [1]})
        self.assertEqual(str(DecisionTreeRegressor(criterion={}).fit(X, y)), "1 (None)")

        X, y = generate_data(
            {
                "A": ["a", "a", "a"],
                "B": [1, 1, 1],
                "y": [
                    2,
                    2,
                    2,
                ],
            }
        )
        self.assertEqual(str(DecisionTreeRegressor(criterion={}).fit(X, y)), "2 (None)")

        X, y = generate_data(
            {"A": ["a", "a", "b", "b"], "B": [3, 1, 2, 5], "y": [1, 2, 3, 4]}
        )
        self.assertEqual(
            str(DecisionTreeRegressor(criterion={}).fit(X, y)),
            "A (None)\n\tB (< 2.0)\n\t\t2\n\t\t1\n\tB (< 3.5)\n\t\t3\n\t\t4",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
