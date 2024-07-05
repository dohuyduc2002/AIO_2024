"""This module define test case for AIO2024 Module 1 week 1 exercise."""
import Week_1.calculate_f1_score as calculate_f1_score
import Week_1.activate_function as activate_function
import Week_1.regression_loss as regression_loss
import Week_1.hyperbolic_approx as hyperbolic_approx
import Week_1.md_rne as md_rne

if __name__ == "__main__":
########### Exercise 1 ###########
    calculate_f1_score.cal_f1_score(2,4,3) # type: ignore
    calculate_f1_score.cal_f1_score('a',4,3) # type: ignore
    calculate_f1_score.cal_f1_score(2,'b',3) # type: ignore
    calculate_f1_score.cal_f1_score(2,4,2.4) # type: ignore
    calculate_f1_score.cal_f1_score(-2,4,3) # type: ignore
    calculate_f1_score.cal_f1_score(2,4,-3) # type: ignore

########### Exercise 2 ###########
    activate_function.activate_function(32.2,"bigmoid") # type: ignore
    activate_function.activate_function('a',"bigmoid") # type: ignore
    activate_function.activate_function(32.2,"RELU") # type: ignore

########### Exercise 3 ###########
    nums = input("input number of samples ") # type: ignore
    loss_func = input('input the loss function ') # type: ignore
    regression_loss.regression_loss(nums, loss_func) # type: ignore

########### Exercise 4 ###########
    hyperbolic_approx.approx_sin( x =3.14 , n =10)
    hyperbolic_approx.approx_cos( x =3.14 , n =10)
    hyperbolic_approx.approx_sinh( x =3.14 , n =10)
    hyperbolic_approx.approx_cosh(x = 3.14, n = 10)

########### Exercise 5 ###########
    md_rne.md_nre_single_sample(y = 100, yhat = 49.5, n = 2, p = 1)
    md_rne.md_nre_single_sample(y = 50, yhat = 99.5, n = 2, p = 1)
    md_rne.md_nre_single_sample(y = 20, yhat = 19.5, n = 2, p = 1)
    md_rne.md_nre_single_sample(y = 0.6, yhat = 0.1, n = 2, p = 1)
