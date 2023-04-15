
# import libraries
import math
import numpy as np
import scipy.stats as st


# 1) Даны две независимые выборки. Не соблюдается условие нормальности
# x1: [380, 420, 290]; y1: [140, 360, 200, 900] 
# Сделайте вывод по результатам, полученным с помощью функции, 
# имеются ли статистические различия между группами?

'''
Mann-Whitney U-test is used for comparing differences between two independent groups. 
It tests the hypothesis that if the two groups come from same population or have the same medians. 
It does not assume any specific distribution (such as normal distribution of samples) 
for calculating test statistics and p-values.
'''

# task 1
def stats_1():

    # datasets    
    arr1 = np.array([380, 420, 290])
    arr2 = np.array([140, 360, 200, 900])

    # level of significance
    alpha = 0.05 

    # perform Mann-Whitney U-test
    results = st.mannwhitneyu(x=arr1, y=arr2, alternative='two-sided')

    # print out result
    print(f'\ntask_1: \n{results}')

    if (results[1] < alpha):
        print('Reject Null Hypothesis\n')
    else:
        print('Fail to Reject Null Hypothesis\n')

stats_1()

'''
Conclusion: there is no difference between two datasets
'''


# 2) Исследовалось влияние препарата на уровень давления пациентов. 
# Сначала измерялось давление до приема препарата, потом через 10 минут и через 30 минут. 
# Есть ли статистически значимые различия между измерениями давления? 
# В выборках не соблюдается условие нормальности.
# 1е измерение до приема препарата: [150, 160, 165, 145, 155]
# 2е измерение через 10 минут: [140, 155, 150, 130, 135]
# 3е измерение через 30 минут: [130, 130, 120, 130, 125]

'''
The Friedman test tests the null hypothesis that repeated samples of the same 
individuals have the same distribution. 
It is often used to test for consistency among samples obtained in different ways. 
For example, if two sampling techniques are used on the same set of individuals, 
the Friedman test can be used to determine if the two sampling techniques are consistent.
'''

# task 2
def stats_2():

    # datasets    
    arr1 = np.array([150, 160, 165, 145, 155])
    arr2 = np.array([140, 155, 150, 130, 135])
    arr3 = np.array([130, 130, 120, 130, 125])

    # level of significance
    alpha = 0.05 

    # perform Friedman test
    results = st.friedmanchisquare(arr1, arr2, arr3)

    # print out result
    print(f'task_2: \n{results}')

    # function outputs p-value which is compared with alpha;
    # if it is greater than alpha then null hypothesis is not rejected else rejected.
    if (results[1] < alpha):
        print('Reject Null Hypothesis\n')
    else:
        print('Fail to Reject Null Hypothesis\n')

stats_2()

'''
Conclusion: there is a difference between three datasets
'''


# 3) Сравните 1 и 2-е измерения, предполагая, что 3-го измерения через 30 минут не было. 
# Есть ли статистически значимые различия между измерениями давления?

'''
The Wilcoxon signed-rank test tests the null hypothesis that two related paired samples 
come from the same distribution. 
In particular, it tests whether the distribution of the differences x - y is symmetric about zero. 
It is a non-parametric version of the paired T-test.
'''

# task 3
def stats_3():

    # datasets    
    arr1 = np.array([150, 160, 165, 145, 155])
    arr2 = np.array([140, 155, 150, 130, 135])

    # level of significance
    alpha = 0.05 

    # perform Wilcoxon signed-rank test
    results = st.wilcoxon(x=arr1, y=arr2)

    # print out result
    print(f'task_3: \n{results}')

    # function outputs p-value which is compared with alpha;
    # if it is greater than alpha then null hypothesis is not rejected else rejected.
    if (results[1] < alpha):
        print('Reject Null Hypothesis\n')
    else:
        print('Fail to Reject Null Hypothesis\n')

stats_3()

'''
Conclusion: there is no difference between two datasets
'''


# 4) Даны 3 группы учеников плавания. Не соблюдается условие нормальности.
# В 1 группе время на дистанцию 50 м составляют: 
# [56, 60, 62, 55, 71, 67, 59, 58, 64, 67]
# Вторая группа : [57, 58, 69, 48, 72, 70, 68, 71, 50, 53]
# Третья группа: [57, 67, 49, 48, 47, 55, 66, 51, 54]
# Есть ли статистически значимые различия между группами?

'''
The Kruskal-Wallis H-test tests the null hypothesis that the population median 
of all of the groups are equal. It is a non-parametric version of ANOVA. 
The test works on 2 or more independent samples, which may have different sizes. 
Note that rejecting the null hypothesis does not indicate which of the groups differs. 
Post hoc comparisons between groups are required to determine which groups are different.
'''

# task 4
def stats_4():

    # datasets    
    arr1 = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
    arr2 = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
    arr3 = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])

    # level of significance
    alpha = 0.05 

    # perform Kruskal-Wallis H-test
    results = st.kruskal(arr1, arr2, arr3)

    # print out result
    print(f'task_4: \n{results}')

    # function outputs p-value which is compared with alpha;
    # if it is greater than alpha then null hypothesis is not rejected else rejected.
    if (results[1] < alpha):
        print('Reject Null Hypothesis\n')
    else:
        print('Fail to Reject Null Hypothesis\n')

stats_4()

'''
Conclusion: there is no difference between three datasets
'''


# 5) Заявляется, что партия изготавливается со средним арифметическим 2.5 см. 
# Проверить данную гипотезу, если известно, что размеры изделий подчинены нормальному закону распределения. 
# Объем выборки 10, уровень статистической значимости 5%
# [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]

# task 5
def stats_5():
    
    # dataset
    arr = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])

    # constants
    n = arr.size # sample size
    avg = 2.5 # mean of the population (mu)
    alpha = 0.05 # level of significance (for 95% confidence)
    
    # stats of the sample
    X_mean = np.mean(arr)
    X_std = np.std(arr)

    # print mean and std
    print('task_5:')
    print('mean=%.2f std=%.2f' % (X_mean, X_std))
    
    # calculate the test statistic
    test_stat = (X_mean - avg) / (X_std / math.sqrt(n))

    # output the p-value of the test statistic (two tailed test)
    p_value = 2 * (1 - st.t.cdf(test_stat, n - 1))
    
    # function outputs p-value which is compared with alpha;
    # if it is greater than alpha then null hypothesis is not rejected else rejected.
    if (p_value < alpha):
        print('Reject Null Hypothesis\n')
    else:
        print('Fail to Reject Null Hypothesis\n')

stats_5()

'''
Conclusion: there is no difference between average value of population
and mean of the sample
'''