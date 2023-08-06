"""@Author Rayane AMROUCHE

ModelManager Class
"""
from typing import Any

from sklearn.base import BaseEstimator   # type: ignore

from dsmanager.datamanager.datastorage import DataStorage


class Model(BaseEstimator):
    """Estimor Class to parametrize model in a pipeline and that inherit from
        sklearn's BaseEstimator
    """

    def __init__(
            self,
            estimator: Any,
    ):
        """Init class Model with an estimator

        Args:
            estimator (Any): estimator
        """

        self.estimator = estimator

    def fit(self, X: Any, y: Any = None, **kwargs) -> Any:  # pylint: disable=invalid-name
        """_summary_

        Args:
            X (Any): _description_
            y (Any, optional): _description_. Defaults to None.

        Returns:
            Any: _description_
        """
        self.estimator.fit(X, y, **kwargs)
        return self

    def predict(self, X: Any) -> Any:  # pylint: disable=invalid-name
        """_summary_

        Args:
            X (Any): _description_

        Returns:
            Any: _description_
        """
        return self.estimator.predict(X)

    def predict_proba(self, X: Any) -> Any:  # pylint: disable=invalid-name
        """_summary_

        Args:
            X (Any): _description_

        Returns:
            Any: _description_
        """
        return self.estimator.predict_proba(X)

    def score(self, X: Any, y: Any = None) -> Any:  # pylint: disable=invalid-name
        """_summary_

        Args:
            X (Any): _description_
            y (Any, optional): _description_. Defaults to None.

        Returns:
            Any: _description_
        """
        return self.estimator.score(X, y)


class ModelManager:
    """ModelManager class handle all the Model work"""

    def __init__(self, models: dict) -> None:
        """_summary_
        """
        self.models = DataStorage(models)

    def load(self):
        """_summary_
        """

    def save(self):
        """_summary_
        """
