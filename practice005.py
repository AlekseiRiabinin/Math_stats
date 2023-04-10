# import libraries
import math
import numpy as np
import scipy.stats as stats
from numpy.random import randn
from scipy.stats import norm 
from statsmodels.stats.weightstats import ztest


# 1) Когда используется критерий Стьюдента, а когда Z –критерий?
''' 
A t-test is any statistical hypothesis test in which the test statistic follows a Student's t-distribution 
under the null hypothesis. It is most commonly applied when the test statistic would follow a normal distribution 
if the value of a scaling term in the test statistic were known (typically, the scaling term is unknown and 
therefore a nuisance parameter). When the scaling term is estimated based on the data, the test statistic—under 
certain conditions—follows a Student's t distribution. The t-test's most common application is to test whether 
the means of two populations are different.
'''

'''
A z-test is any statistical test for which the distribution of the test statistic under the null hypothesis can be 
approximated by a normal distribution. Z-tests test the mean of a distribution. For each significance level in the 
confidence interval, the Z-test has a single critical value (for example, 1.96 for 5% two tailed) which makes it 
more convenient than the Student's t-test whose critical values are defined by the sample size (through the 
corresponding degrees of freedom). Both the Z-test and Student's t-test have similarities in that they both help 
determine the significance of a set of data. However, the z-test is rarely used in practice because the population 
deviation is difficult to determine.
'''

# 2) Провести тест гипотезы. 
# Утверждается, что шарики для подшипников, изготовленные автоматическим станком, имеют средний диаметр 17 мм.
# Используя односторонний критерий с α=0.05, проверить эту гипотезу, 
# если в выборке из n=100 шариков средний диаметр оказался равным 17.5 мм, а дисперсия известна и равна 4 кв. мм.

# task 2
def stats_2():
    
    # constants
    n = 100 # sample size
    avg = 17 # mean of the population (mu)
    var = 4 # variance of the sample
    X_mean = 17.5 # mean of the sample
    alpha = 0.05 # level of significance
    
    # std of the population
    std = math.sqrt(var) / math.sqrt(n)

    # generate a random array of 100 numbers having avg = 17mm and std = 4mm2
    data = std * randn(n) + X_mean
    
    # print mean and std
    print('\ntask_2:')
    print('mean=%.2f std=%.2f' % (np.mean(data), np.std(data)))
    
    # for the value parameter mean value is passed in the null hypothesis; 
    # alternative hypothesis checks whether the mean is larger.
    # ztest_Score, p_value = ztest(data, value=avg, alternative='larger')
    
    # calculate z-score
    z_score = (X_mean - avg) / std
    
    # calculate p-value for left-sided tail test (avg < X_mean)
    p_value = norm.cdf(z_score)
    
    # function outputs p-value and z-score corresponding to that value, p-value is compared with alpha;
    # if it is greater than alpha then null hypothesis is not rejected else rejected.
    if (p_value < alpha):
        print('Reject Null Hypothesis\n')
    else:
        print('Fail to Reject Null Hypothesis\n')

stats_2()        

# 3) Проведите тест гипотезы. 
# Продавец утверждает, что средний вес пачки печенья составляет 200 г.
# Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
# [202, 203, 199, 197, 195, 201, 200, 204, 194, 190].
# Известно, что их веса распределены нормально.
# Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%? 
# (Провести двусторонний тест)

# task 3
def stats_3():
    
    # dataset
    arr = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])

    # constants
    n = arr.size # sample size
    avg = 200 # mean of the population (mu)
    alpha = 0.01 # level of significance (for 99% confidence)
    
    # stats of the sample
    X_mean = np.mean(arr)
    X_std = np.std(arr)

    # print mean and std
    print('task_3:')
    print('mean=%.2f std=%.2f' % (X_mean, X_std))
    
    # calculate the test statistic
    test_stat = (X_mean - avg) / (X_std / math.sqrt(n))

    # output the p-value of the test statistic (two tailed test)
    p_value = 2 * (1 - stats.t.cdf(test_stat, n - 1))
    
    # function outputs p-value which is compared with alpha;
    # if it is greater than alpha then null hypothesis is not rejected else rejected.
    if (p_value < alpha):
        print('Reject Null Hypothesis\n')
    else:
        print('Fail to Reject Null Hypothesis\n')

stats_3()

# 4) Есть ли статистически значимые различия в росте дочерей?
# Рост матерей: [172, 177, 158, 170, 178,175, 164, 160, 169, 165]
# Рост взрослых дочерей: [173, 175, 162, 174, 175, 168, 155, 170, 160, 163]

def stats_4():
    
    # datasets
    arr1 = np.array([172, 177, 158, 170, 178,175, 164, 160, 169, 165])
    arr2 = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160, 163])

    alpha = 0.05 # level of significance

    # print the variance of both data groups
    print('task_4:')
    print('stats1=%.2f stats2=%.2f' % (np.var(arr1), np.var(arr2)))

    # perform the two sample t-test with equal variances
    anal_results = stats.ttest_ind(a=arr1, b=arr2, equal_var=True)
    print(anal_results)

    # H0 => µ1 = µ2 (population mean of arr1 is equal to arr2)
    # HA => µ1 ≠ µ2 (population mean of arr1 is different from arr2)
    if (anal_results[1] < alpha):
        print('Reject Null Hypothesis\n')
    else:
        print('Fail to Reject Null Hypothesis\n')
    
stats_4()    