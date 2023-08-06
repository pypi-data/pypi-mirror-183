"""Module containing the parallel random forest classifier implementation."""

from statistics import mode

import numpy as np
import pandas as pd
from mpi4py import MPI
from sklearn.metrics import accuracy_score

from .parallel_decision_tree import ParallelDecisionTreeClassifier

world_comm = MPI.COMM_WORLD
world_rank = world_comm.Get_rank()
world_size = world_comm.Get_size()


def maj_vote(*argv):
    """Reduces the 2D array to a 1D array by means of the mode"""
    if len(argv) == 1:
        return argv[0]
    for arg in argv:
        if arg is None:
            continue
        return list(map(mode, list(zip(maj_vote(arg)))))


MODE = MPI.Op.Create(maj_vote, commute=True)


class ParallelRandomForestClassifier:
    """A Rudimentary Parallel Random Forest Classifier"""

    def __init__(self, n_sample=2, criterion=None):
        self.n_sample = n_sample
        self.tree = ParallelDecisionTreeClassifier(criterion=criterion)

    def sub_sample(self, X, n_sample=2):
        """Enforces feature randomness."""
        return np.random.choice(X.columns.to_numpy(), n_sample, replace=False)

    def _bootstrap_sample(self, X, y, n_sample, key=True):
        """Computes the bootstrap samples for each decision tree."""
        feature_subset = self.sub_sample(X, int(np.log2(len(X.columns))))
        d = pd.concat([X, y], axis=1)
        d = d.sample(n=n_sample, replace=key, random_state=42)
        return d.iloc[:, :-1][feature_subset], d.iloc[:, -1]

    def fit(self, X, y):
        """Fits the random forest classifier to the dataset."""
        self.tree.fit(*self._bootstrap_sample(X, y, self.n_sample))
        return self

    def score(self, X, y):
        """Evalutes the random forest model on the test set."""
        assert isinstance(self.tree, ParallelDecisionTreeClassifier)
        pred = [
            self.tree.predict(X.iloc[x].to_frame().T).feature for x in range(len(X))
        ]
        y_hat = world_comm.allreduce(np.array(pred).T, op=MODE)
        return accuracy_score(y, y_hat)
