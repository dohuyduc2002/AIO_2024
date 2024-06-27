"""This module define function for AIO2024 Module 1 week 1 exercise."""
import math
import random

def mae(y : float, yhat : float) -> float:
    """_summary_

    Args:
        y (float): Observed value
        yhat (float): Predicted value

    Returns:
        mae: Mean Absolute Error
    """
    func = abs(y - yhat)
    return func

def mse(y : float, yhat : float) -> float:
    """_summary_

    Args:
        y (float): Observed value
        yhat (float): Predicted value

    Returns:
        mse: Mean Square Error
    """
    func = (y - yhat) ** 2
    return func

def rmse(y : float, yhat: float) -> float:
    """_summary_

    Args:
        y (float): Observed value
        yhat (float): Predicted value

    Returns:
        rmse: Root Mean Square Error
    """
    func = math.sqrt((y - yhat)**2)
    return func

def regression_loss(n : int ,loss_function : str) -> float:
    """_summary_

    Args:
        n (int): Number of sample
        loss_function (str): Desire loss function [MSE, MAE,RMSE]

    Returns:
        final_loss: Loss according to loss function name
    """
    if isinstance(n, int): # type: ignore
        n = str(n) # type: ignore
    if n.isnumeric() is False: # type: ignore
        print('number of samples must be an integer number')
        return 1
    else:
        n = int(n)

    final_loss = 0
    loss_function = loss_function.lower()
    for i in range(n):
        loss = 0
        y = random.uniform(0, 10)
        yhat = random.uniform(0, 10)

        if loss_function == 'mae':
            loss += mae(y, yhat)
        elif loss_function == 'mse':
            loss += mse(y, yhat)
        elif loss_function == 'rmse':
            loss += mse(y, yhat)
        print(f"loss name: {loss_function}, sample: {i}, pred: {yhat}, target: {y}, loss {loss}")
    if loss_function == 'mae' or 'mse':
        final_loss = loss / n # type: ignore
        print(f"final loss for {loss_function} is {final_loss}")
    elif loss_function == 'rmse':
        final_loss = math.sqrt(loss / n) # type: ignore
        print(f"final loss for {loss_function} is {final_loss}")
    return final_loss

#nums = input("input number of samples ")
#loss_func = input('input the loss function ')
#regression_loss(nums, loss_func) # type: ignore
