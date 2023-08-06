"""Module containing the random forest classifier and regressor implementations."""

from statistics import mean, mode

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, mean_squared_error

from .decision_tree import DecisionTreeClassifier, DecisionTreeRegressor


class RandomForestClassifier:
    """A Rudimentary Random Forest Classifier"""

    def __init__(self, *, n_estimators=5, n_sample=0, criterion=None):
        self.n_estimators = n_estimators
        self.n_sample = n_sample
        self.forest = [
            DecisionTreeClassifier(criterion=criterion) for _ in range(n_estimators)
        ]

    def __str__(self):
        """Outputs all decision trees in the forest."""
        return "\n".join(map(str, self.forest))

    def _sub_sample(self, X, n_sample=2):
        """Enforces feature randomness."""
        return np.random.choice(X.columns.to_numpy(), n_sample, replace=False)

    def _bootstrap_sample(self, X, y, n_sample, key=True):
        """Computes the bootstrap samples for each decision tree."""
        feature_subset = self._sub_sample(X, int(np.log2(len(X.columns))))
        d = pd.concat([X, y], axis=1)
        d = d.sample(n=n_sample, replace=key, random_state=42)
        return d.iloc[:, :-1][feature_subset], d.iloc[:, -1]

    def fit(self, X, y):
        """Fits the random forest regressor to the dataset."""
        for tree in self.forest:
            tree.fit(*self._bootstrap_sample(X, y, self.n_sample))
        return self

    def predict(self, x):
        """Predicts a test sample on a random forest classifier."""
        assert all(isinstance(model, DecisionTreeClassifier) for model in self.forest)
        return mode([dt.predict(x).feature for dt in self.forest])

    def score(self, X, y):
        """Evalutes the random forest model on the test set."""
        y_hat = [self.predict(X.iloc[x].to_frame().T) for x in range(len(X))]
        return accuracy_score(y, y_hat)


class RandomForestRegressor:
    """A Rudimentary Random Forest Regressor"""

    def __init__(self, *, n_estimators=5, n_sample=0, criterion=None):
        self.n_estimators = n_estimators
        self.n_sample = n_sample
        self.forest = [
            DecisionTreeRegressor(criterion=criterion) for _ in range(n_estimators)
        ]

    def __str__(self):
        """Outputs all decision trees in the forest."""
        return "\n".join(map(str, self.forest))

    def _sub_sample(self, X, n_sample=2):
        """Enforces feature randomness."""
        return np.random.choice(X.columns.to_numpy(), n_sample, replace=False)

    def _bootstrap_sample(self, X, y, n_sample, key=True):
        """Computes the bootstrap samples for each decision tree."""
        feature_subset = self._sub_sample(X, int(np.log2(len(X.columns))))
        d = pd.concat([X, y], axis=1)
        d = d.sample(n=n_sample, replace=key, random_state=42)
        return d.iloc[:, :-1][feature_subset], d.iloc[:, -1]

    def fit(self, X, y):
        """Fits the random forest regressor to the dataset."""
        for tree in self.forest:
            tree.fit(*self._bootstrap_sample(X, y, self.n_sample))
        return self

    def predict(self, x):
        """Predicts a test sample on a random forest regressor."""
        assert all(isinstance(model, DecisionTreeRegressor) for model in self.forest)
        return mean([dt.predict(x).feature for dt in self.forest])

    def score(self, X, y):
        """Evalutes the random forest model on the test set."""
        y_hat = [self.predict(X.iloc[x].to_frame().T) for x in range(len(X))]
        return mean_squared_error(y, y_hat, squared=False)
