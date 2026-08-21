"""Ensemble-defended NIDS classifier.

TODO: implement a small ensemble (e.g., gradient-boosted trees + a
feed-forward net) with disagreement-based abstention as a defense layer.
"""


class EnsembleNIDS:
    def fit(self, x_train, y_train):
        raise NotImplementedError

    def predict(self, x):
        raise NotImplementedError
