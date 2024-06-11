"""This module define function for AIO2024 Module 1 week 1 exercise."""
import math


def md_nre_single_sample(n: int, p : int, y : float, yhat: float) -> float:
    """Calulate Mean difference n^th root error

    Args:
        n (int): Number of root taken
        m (int): Number of simulation
        y (float): Observed value
        yhat (float): Predicted value

    Returns:
        float: Mean difference n^th root error
    """
    diff_single_error = math.pow(math.pow(y, 1/n) - math.pow(yhat,1/n),p)
    print(f"Difference {n} root for single error is: {diff_single_error}")
    return diff_single_error
