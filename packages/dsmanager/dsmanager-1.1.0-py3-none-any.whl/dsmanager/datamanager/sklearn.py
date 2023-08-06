"""@Author: Rayane AMROUCHE

Sklearn classes rewritten
"""

from typing import Any

import numpy as np  # type: ignore

from sklearn.compose import ColumnTransformer  # type: ignore
from sklearn.impute import KNNImputer  # type: ignore
from sklearn.utils.validation import check_is_fitted  # type: ignore


class DSMKNNInputer(KNNImputer):
    """Adds an inverse transform method to the standard
        sklearn.impute.KNNImputer.
    """

    def inverse_transform(self, X: Any) -> Any:  # pylint: disable=invalid-name
        """Convert the data back to the original representation.

        Args:
            X (Any): {array-like, sparse matrix} of shape
                (n_samples, n_encoded_features). Transformed data.

        Returns:
            Any: ndarray of shape (n_samples, n_features) Inverse transformed
                array.
        """
        check_is_fitted(self)

        X[self._mask_fit_X] = self.missing_values
        return X


class DSMColumnTransformer(ColumnTransformer):
    """Adds an inverse transform method to the standard
        sklearn.compose.ColumnTransformer.
    """

    def __init__(
        self,
        transformers,
        *,
        remainder="drop",
        sparse_threshold=0.3,
        n_jobs=None,
        transformer_weights=None,
        verbose=False,
        verbose_feature_names_out=False,
    ):
        super().__init__(
            transformers=transformers,
            remainder=remainder,
            sparse_threshold=sparse_threshold,
            n_jobs=n_jobs,
            transformer_weights=transformer_weights,
            verbose=verbose,
            verbose_feature_names_out=verbose_feature_names_out
        )

    def inverse_transform(self, X: Any) -> Any:  # pylint: disable=invalid-name
        """Convert the data back to the original representation.

        Args:
            X (Any): {array-like, sparse matrix} of shape
                (n_samples, n_encoded_features). Transformed data.

        Raises:
            Exception: Raised if X and the fitted transformer seem to have
                different numbers of columns.

        Returns:
            Any: ndarray of shape (n_samples, n_features) Inverse transformed
                array.
        """

        if X.shape[1] != self.n_features_in_:
            raise Exception(
                "X and the fitted transformer seem to have different numbers of columns.")

        arrays = []

        for name, indices in self.output_indices_.items():
            transformer = self.named_transformers_.get(name, None)
            arr = X.iloc[:, indices]

            if transformer is None:
                pass

            else:
                arr = transformer.inverse_transform(arr)

            arrays.append(arr)

        return np.concatenate(arrays, axis=1)
