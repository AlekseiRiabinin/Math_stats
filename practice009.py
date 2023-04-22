# import libraries
import numpy as np
import matplotlib.pyplot as plt


# 1) Даны значения величины заработной платы заемщиков банка (zp) и значения их
# поведенческого кредитного скоринга (ks): 
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. 
# Используя математические операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату
# (то есть, zp - признак), а за y - значения скорингового балла (то есть, ks - целевая переменная). 
# Произвести расчет как с использованием intercept, так и без.

# datasets
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110]) 
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# task 1
def stats_1(X, y):
    
    # size of dataset
    n = np.size(X)
    
    # mean values
    X_mean = np.mean(X)
    y_mean = np.mean(y)

    # sample covariance (Sxy) and variance (Sxx)     
    Sxy = np.sum(X * y) - n * X_mean * y_mean
    Sxx = np.sum(X * X) - n * X_mean * X_mean
    
    # linear regression coefficients
    b1 = Sxy / Sxx # slope
    b0 = y_mean - b1 * X_mean # intercept
    
    # print out results
    print('\ntask_1\n------')
    print(f'slope b1: {b1}\nintercept b0: {b0}\n')

stats_1(zp, ks)


# 2) Посчитать коэффициент линейной регрессии при заработной плате (zp), 
# используя градиентный спуск (без intercept).

# task 2
def stats_2(X, y):

    # initialize coefficient
    m = 0 # slope (b1)

    # hyperparameters
    LEARN_RATE = 0.01 # learning rate
    EPOCHS = 100 # number of iterations to perform gradient descent

    n = float(len(X)) # number of elements in dataset

    # perform Gradient Descent 
    for i in range(EPOCHS): 
        
        # current predicted value of y
        y_pred = m * X 
        
        # calculate derivative wrt m
        D_m = (-2 / n) * sum(X * (y - y_pred))
        
        # update parameters
        m = m - LEARN_RATE * D_m
        
    # print out results
    print('task_2\n------')
    print(f'slope b1: {m}\n')

stats_2(zp, ks)


# 3) Произвести вычисления как в пункте 2, но с вычислением intercept. 
# Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно 
# (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации)

# task 3
def stats_3(X, y):

    # initialize coefficients
    m = 0 # slope (b1)
    c = 0 # intercept (b0)

    # hyperparameters
    LEARN_RATE = 0.01 # learning rate
    EPOCHS = 100 # number of iterations to perform gradient descent

    n = float(len(X)) # number of elements in dataset

    # perform Gradient Descent 
    for i in range(EPOCHS): 
        
        # current predicted value of y
        y_pred = m * X + c 
        
        # calculate derivatives wrt m and wrt c
        D_m = (-2 / n) * sum(X * (y - y_pred))
        D_c = (-2 / n) * sum(y - y_pred)
        
        # update parameters
        m = m - LEARN_RATE * D_m
        c = c - LEARN_RATE * D_c
        
    # print out results
    print('task_3\n------')
    print(f'slope b1: {m}\nintercept b0: {c}\n')

stats_3(zp, ks)