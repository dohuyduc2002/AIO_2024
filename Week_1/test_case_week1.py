"""This module define test case for AIO2024 Module 1 week 1 exercise."""
import exercise_1
import exercise_2
import exercise_3
import exercise_4
import exercise_5

if __name__ == "__main__":
########### Exercise 1 ###########
    exercise_1.cal_f1_score(2,4,3) # type: ignore
    exercise_1.cal_f1_score('a',4,3) # type: ignore
    exercise_1.cal_f1_score(2,'b',3) # type: ignore
    exercise_1.cal_f1_score(2,4,2.4) # type: ignore
    exercise_1.cal_f1_score(-2,4,3) # type: ignore
    exercise_1.cal_f1_score(2,4,-3) # type: ignore

########### Exercise 2 ###########
    exercise_2.activate_function(32.2,"bigmoid") # type: ignore
    exercise_2.activate_function('a',"bigmoid") # type: ignore
    exercise_2.activate_function(32.2,"RELU") # type: ignore

########### Exercise 3 ###########
    nums = input("input number of samples ") # type: ignore
    loss_func = input('input the loss function ') # type: ignore
    exercise_3.regression_loss(nums, loss_func) # type: ignore

########### Exercise 4 ###########
    exercise_4.approx_sin( x =3.14 , n =10)
    exercise_4.approx_cos( x =3.14 , n =10)
    exercise_4.approx_sinh( x =3.14 , n =10)
    exercise_4.approx_cosh(x = 3.14, n = 10)

########### Exercise 5 ###########
    exercise_5.md_nre_single_sample(y = 100, yhat = 49.5, n = 2, p = 1)
    exercise_5.md_nre_single_sample(y = 50, yhat = 99.5, n = 2, p = 1)
    exercise_5.md_nre_single_sample(y = 20, yhat = 19.5, n = 2, p = 1)
    exercise_5.md_nre_single_sample(y = 0.6, yhat = 0.1, n = 2, p = 1)
