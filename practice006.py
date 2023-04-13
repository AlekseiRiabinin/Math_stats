# import libraries
import numpy as np 
import scipy.stats as st
from statsmodels.stats.weightstats import DescrStatsW, CompareMeans


# 1) Известно, что генеральная совокупность распределена нормально со средним 
# квадратическим отклонением, равным 16.
# Найти доверительный интервал для оценки математического ожидания с надежностью 0.95, 
# если выборочная средняя M = 80, а объем выборки n = 256.

# task 1
def stats_1():
    
    # constants
    mean = 80 # mean value
    std = 16 # standard deviation
    n = 256 # size of dataset
    conf = 0.95 # confidence

    # degrees of freedom
    dof = n - 1 

    # calculate t-score using inverse cumulative distribution (ppf)
    t_crit = np.abs(st.t.ppf(q=(1-conf)/2, df=dof))

    # calculate confidence interval
    lower = mean - std * t_crit / np.sqrt(n) 
    upper = mean + std * t_crit / np.sqrt(n)

    # print out result
    print(f'\ntask_1: ({lower}, {upper})\n')

stats_1()


# 2) В результате 10 независимых измерений некоторой величины X, 
# выполненных с одинаковой точностью, получены опытные данные:
# [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
# Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей, 
# оценить истинное значение величины X при помощи доверительного интервала, 
# покрывающего это значение с доверительной вероятностью 0.95

# task 2
def stats_2():

    # dataset
    arr = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
    
    # create 95% confidence interval
    result = st.t.interval(
        alpha=0.95, 
        df=len(arr)-1, 
        loc=np.mean(arr), 
        scale=st.sem(arr)
    )

    # print out result
    print(f'task_2: {result}\n')

stats_2()


# 3) Рост дочерей [175, 167, 154, 174, 178, 148, 160, 167, 169, 170]
# Рост матерей [178, 165, 165, 173, 168, 155, 160, 164, 178, 175]
# Используя эти данные построить 95% доверительный интервал для разности среднего роста 
# родителей и детей.

# task 3
def stats_3 ():

    # datasets
    arr1 = [175, 167, 154, 174, 178, 148, 160, 167, 169, 170]
    arr2 = [178, 165, 165, 173, 168, 155, 160, 164, 178, 175]

    # confidence
    conf = 0.95

    # size of datasets
    n = len(arr1) 
    m = len(arr2)
    
    # standard deviation
    std1 = np.std(arr1, ddof=1)
    std2 = np.std(arr2, ddof=1)
    
    # degrees of freedom using Welch–Satterthwaite equation
    # https://en.wikipedia.org/wiki/Welch%27s_t-test
    num = (std1 ** 2 / n + std2 ** 2 / m) ** 2
    den = ((std1 ** 2 / n) ** 2) / (n - 1) + ((std2 ** 2 / m) ** 2) / (m - 1)
    dof = num / den
    
    # difference of means
    diff = np.mean(arr1) - np.mean(arr2)

    # calculate confidence interval
    lower_main = diff + st.t.ppf(q=1-conf, df=dof) * np.sqrt(std1 ** 2 / n + std2 ** 2 / m)
    upper_main = diff - st.t.ppf(q=1-conf, df=dof) * np.sqrt(std1 ** 2 / n + std2 ** 2 / m)

    # check results (Welch ttest with Satterthwait degrees of freedom)
    cm = CompareMeans(d1=DescrStatsW(data=arr1), d2=DescrStatsW(data=arr2))
    lower_check, upper_check = cm.tconfint_diff(
        alpha=0.05, 
        alternative='two-sided', 
        usevar='unequal'
    )
    
    # print out results
    print(f'task_3_1: ({lower_main}, {upper_main})')
    print(f'task_3_2: ({lower_check}, {upper_check})\n')

stats_3()   