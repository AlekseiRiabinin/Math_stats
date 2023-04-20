# import libraries
import numpy as np
import scipy.stats as st


# 1) Даны значения величины заработной платы заемщиков банка (zp) и 
# значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий, 
# а затем с помощью функции cov из numpy. Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков, 
# а затем с использованием функций из библиотек numpy и pandas.

# task 1
zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]

# find individual q_jk covariance values given two vectors of a matrix (v_j, v_k)
def cov_value(x, y):
    
    # mean of both vectors
    mean_x = sum(x) / float(len(x))
    mean_y = sum(y) / float(len(y))
    
    # difference between true and mean values
    sub_x = [i - mean_x for i in x]
    sub_y = [i - mean_y for i in y]
    
    # sum of differences
    sum_value = sum([sub_y[i] * sub_x[i] for i in range(len(x))])
    denom = float(len(x) - 1)
    
    # covarience
    cov = sum_value / denom
    return cov

# check lenght of vectors
def check_vectors(arr):

    # build temp array for checking
    length = len(arr[0])
    x = [1 for a in arr if len(a) != length]
    
    if (sum(x) > 0):
        raise Exception(f'length of vectors not the same')

# calculate covariance values for each cell in the matrix
def covariance(x, y):

    # combine vectors into an array
    arr = np.array([x, y])
    
    # check lengths of vectors
    check_vectors(arr)   
    
    # manual calculation
    cov1 = [[cov_value(a, b) for a in arr] for b in arr]
    
    # standard function
    cov2 = (np.cov(x, y)).tolist()

    return cov1, cov2
    
# print out results
def print_covarience():
    cov1, cov2 = covariance(zp, ks)
    print('\ntask_1\n------')
    print(f'covar_1: {cov1}\ncovar_2: {cov2}\n')

print_covarience()

# find Pearson coefficients
def pearson(x, y):

    # manual calculation
    cov, _, = covariance(x, y)
    pear1 = (cov / (np.std(x) * np.std(y))).tolist()

    # standard function
    pear2 = np.corrcoef(x, y).tolist()

    print(f'pearson_1: {pear1}\npearson_2: {pear2}\n')

pearson(zp, ks)


# 2) Измерены значения IQ выборки студентов, обучающихся в местных технических вузах:
# [131, 125, 115, 122, 131, 115, 107, 99, 125, 111].
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

# task 2
def stats_2():

    # dataset
    arr = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]
    
    # create 95% confidence interval
    result = st.t.interval(
        alpha=0.95, 
        df=len(arr)-1, 
        loc=np.mean(arr), 
        scale=st.sem(arr)
    )

    # print out result
    print('task_2\n------')
    print(f'{result}\n')

stats_2()


# 3) Известно, что рост футболистов в сборной распределен нормально 
# с дисперсией генеральной совокупности, равной 25 кв.см. 
# Объем выборки равен 27, среднее выборочное составляет 174.2. 
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

# task 3
def stats_3():
    
    # constants
    mean = 174.2 # mean value
    var = 25 # variance
    n = 27 # size of dataset
    conf = 0.95 # confidence

    # degrees of freedom
    dof = n - 1 

    # calculate t-score using inverse cumulative distribution (ppf)
    t_crit = np.abs(st.t.ppf(q=(1-conf)/2, df=dof))

    # calculate confidence interval
    lower = mean - np.sqrt(var) * t_crit / np.sqrt(n) 
    upper = mean + np.sqrt(var) * t_crit / np.sqrt(n)

    # print out result
    print('task_3\n------')
    print(f'({lower}, {upper})\n')

stats_3()