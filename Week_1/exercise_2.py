"""This module define function for AIO2024 Module 1 week 1 exercise."""
import math

def is_number(n : int) -> bool:
    """Checking number

    Args:
        n (int): Input

    Returns:
        bool: check if n is a number
    """
    try:
        float(n)
    except ValueError:
        return False
    return True

def sigmoid(x : float) -> float:
    """Build sigmoid function

    Args:
        x (float): input

    Returns:
        float: output of sigmoid function
    """
    y = 1 / (1 + math.e ** (-x))
    return y

def relu(x : float) -> float:
    """Build ReLU function

    Args:
        x (float): input

    Returns:
        float: output of ReLU function
    """
    if x <= 0:
        y = 0
        return y
    else:
        y = x
        return y

def elu(x : float, alpha : float = 0.01) -> float:
    """Build ELU function

    Args:
        x (float): input
        alpha (float, optional): parameter of ELU if x <= 0. Defaults to 0.01.

    Returns:
        float: output of ELU function
    """
    if x <= 0:
        y = alpha * (math.e ** x - 1)
        return y
    else:
        y = x
        return y

def activate_function(x : int,function : str) -> float:
    """Activate function using Sigmoid, ELU, ReLU

    Args:
        x (int): Input
        function (str): Desire activate function
    """
    function = function.lower()
    assert is_number(x), "x must be a number"
    if function == "sigmoid":
        y = sigmoid(x)
        print(f"Input activation Function (sigmoid|relu|elu): {function}\n {function}:f({x}) = {y}")
        return y
    elif function == "relu":
        y = relu(x)
        print(f"Input activation Function (sigmoid|relu|elu): {function}\n {function}:f({x}) = {y}")
        return y
    elif function == "elu":
        y = elu(x)
        print(f"Input activation Function (sigmoid|relu|elu): {function}\n {function}:f({x}) = {y}")
        return y
    else:
        print(f"Not support {function} function")
        return 1
# Function test case
#activate_function(32.2,"bigmoid")
#activate_function('a',"bigmoid")
#activate_function(32.2,"RELU")
