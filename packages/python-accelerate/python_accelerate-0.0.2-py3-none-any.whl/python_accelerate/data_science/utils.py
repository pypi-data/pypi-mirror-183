import numpy as np
import numpy.typing as npt


def calculate_iqr(data: npt.ArrayLike) -> np.dtype[np.float64]:
    """ Calculates the IQR (interquartile range) for a given array of values.

    There is already an available library under scipy.stats for this, but this wrapper method around numpy is slightly
    faster.

    Args:
       data (array_like): The values for which the IQR will be computed.

    Returns:
       The IQR of <data> as a np.float64 value.
    """
    q1, q3 = np.percentile(data, [25, 75])
    return q3 - q1


def iqr_outlier_detection(data: npt.ArrayLike, threshold_factor: float = 1.5) -> npt.NDArray[np.dtype[np.bool_]]:
    """ Detects outliers using the IQR method.

    Any values further than <threshold_factor> * IQR from the median are detected as outliers.

    Args:
       data (array_like): The values on which we want to apply outlier detection.
       threshold_factor (float): Used to calculate the range beyond which we detect everything as outliers.
         Defaults to 1.5.

   Returns:
      A numpy array of the same dimensionality as <data>, where an element is True if the element with the same index in
      <data> is an outlier or False otherwise.
    """
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1
    lower_bound = q1 - (threshold_factor * iqr)
    upper_bound = q3 + (threshold_factor * iqr)
    return (data > upper_bound) | (data < lower_bound)
