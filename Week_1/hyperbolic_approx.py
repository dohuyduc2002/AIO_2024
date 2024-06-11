"""This module define function for AIO2024 Module 1 week 1 exercise."""
import math

def factorial(x : int) -> int:
    """Calculate factorial using recursion

    Args:
        x (int): Number of factorial

    Returns:
        int: Factorial of x
    """
    if x == 1 or x == 0:
        return 1
    else:
        y =x * factorial(x - 1)
        return y #Recrusion

def approx_sin(x : float,n : int) -> float:
    """Approximate geometric Sin function

    Args:
        x (float): Pi value
        n (int): Number of simulation 

    Returns:
        float: approximated Sin
    """
    sin = 0
    for i in range(n):
        sin += pow(-1,i) * (x ** (2 * i + 1) / math.factorial(2 * i + 1))
    print(f"Approximate Sin is {sin} after {n} simulation")
    return sin

def approx_cos(x : float,n : int) -> float:
    """Approximate geometric Cosine function

    Args:
        x (float): Pi value
        n (int): Number of simulation

    Returns:
        float: approximated Cosine
    """
    cos = 0
    for i in range(n):
        cos += pow(-1,i) * (pow(x, 2 * i) / math.factorial(2 * i))
    print(f"Approximate Cosine is {cos} after {n} simulation")
    return cos

def approx_sinh(x : float,n: int) -> float:
    """"Approximate geometric Sinh function


    Args:
        x (float): Pi value
        n (int): Number of simulation

    Returns:
        float: approximated Sinh
    """
    sinh = 0
    for i in range(n):
        sinh += pow(x, (2 * i + 1)) / math.factorial(2 * i + 1)
    print(f"Aproximate Sinh is {sinh} after {n} simulation")
    return sinh

def approx_cosh(x : float, n : int) -> float:
    """Approximate geometric Sinh function

    Args:
        x (float): Pi value
        n (int): Number of simulation

    Returns:
        float: approximated Cosh
    """
    cosh = 0
    for i in range(n):
        cosh += pow(x, 2 * i) / math.factorial(2 * i)
    print(f"Approximate Cosh is {cosh} after {n} simulation")
    return cosh
