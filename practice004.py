# import libraries
import math
import numpy as np
import statistics as st
from scipy.stats import norm 


# 1) Случайная непрерывная величина A имеет равномерное распределение на промежутке [200, 800].
# Найдите ее среднее значение и дисперсию.

# task 1
def stats_1():
    
    # vector
    arr = np.arange(200, 800+1)
    
    # calculate stats
    arr_avg = np.mean(arr)
    arr_var = np.var(arr, ddof=0)
    
    # print out results
    print('\ntask_1:')
    print(f'avg: {arr_avg}\nvar: {arr_var}\n')

stats_1()


# 2) О случайной непрерывной равномерно распределенной величине B известно, 
# что ее дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5?
# Если да, найдите ее.

# task 2
def stats_2():

    std = np.sqrt(0.2) # standard deviation
    arr = np.arange(-0.5, 0.5, 0.01) # normal distribution
    n = arr.size # sample size

    # calculate mean
    mean = std / np.sqrt(n)

    # print out result
    print('task_2:')
    print(f'avg: {mean}\n')

stats_2()


# 3) Непрерывная случайная величина X распределена нормально и задана плотностью распределения
# f(x) = (1 / (4 * sqrt(2pi))) * exp((-(x+2)**2) / 32)
# Найти:
# а). M(X)
# б). D(X)
# в). std(X) (среднее квадратичное отклонение)

# task 3
def stats_3():
    
    # define function
    # M(X) = -2; D(X) = 4**2
    arr = np.random.rand(200, 800+1)
    func = lambda x: (1 / (4 * np.sqrt(2 * np.pi))) * np.exp((-(x + 2) ** 2) / 32)
    
    # calculate stats
    arr_avg = np.mean(func(arr))
    arr_var = np.var(func(arr), ddof=0)
    arr_std = np.std(func(arr))

    # print out results
    print('task_3:')
    print(f'avg: {arr_avg}\nvar: {arr_var}\nstd: {arr_std}\n')

stats_3()


# 4) Рост взрослого населения города X имеет нормальное распределение, 
# причем, средний рост равен 174 см, а среднее квадратическое отклонение равно 8 см. 
# Посчитать, какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# 1. больше 182 см?
# 2. больше 190 см?
# 3. от 166 см до 190 см?
# 4. от 166 см до 182 см?
# 5. от 158 см до 190 см?
# 6. не выше 150 см или не ниже 190 см?
# 7. не выше 150 см или не ниже 198 см?
# 8. ниже 166 см?

# task 4
def stats_4():

    # probability of height to be above 182 cm
    prob_1 = 1 - norm(loc=174, scale=8).cdf(182)

    # probability of height to be above 190 cm
    prob_2 = 1 - norm(loc=174 , scale=8).cdf(190)

    # probability that the height of the person to be between 166 and 190 cm
    cdf_3_upper_limit = norm(loc=174 , scale=8).cdf(190)
    cdf_3_lower_limit = norm(loc=174, scale=8).cdf(166)
    prob_3 = cdf_3_upper_limit - cdf_3_lower_limit

    # probability that the height of the person to be between 166 and 182 cm
    cdf_4_upper_limit = norm(loc=174 , scale=8).cdf(182)
    cdf_4_lower_limit = norm(loc=174, scale=8).cdf(166)
    prob_4 = cdf_4_upper_limit - cdf_4_lower_limit

    # probability that the height of the person is between 158 and 190 cm
    cdf_5_upper_limit = norm(loc=174 , scale=8).cdf(190)
    cdf_5_lower_limit = norm(loc=174, scale=8).cdf(158)
    prob_5 = cdf_5_upper_limit - cdf_5_lower_limit

    # probability that the height of the person to be under 150 and above 190 cm
    prob_6_under = norm(loc=174 , scale=8).cdf(150)
    prob_6_above = 1 - norm(loc=174 , scale=8).cdf(190)
    prob_6 = prob_6_under + prob_6_above # logical OR
    
    # probability that the height of the person to be under 150 and above 198 cm
    prob_7_under = norm(loc=174 , scale=8).cdf(150)
    prob_7_above = 1 - norm(loc=174 , scale=8).cdf(198)
    prob_7 = prob_7_under + prob_7_above # logical OR
    
    # probability of height to be under 166 cm
    prob_8 = norm(loc=174 , scale=8).cdf(166)

    # print out results
    print('task_4:')
    print('(1): {}\n(2): {}\n(3): {}\n(4): {}\n(5): {}\n(6): {}\n(7): {}\n(8): {}\n'\
          .format(prob_1, prob_2, prob_3, prob_4, prob_5, prob_6, prob_7, prob_8))

stats_4()


# 5) На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см, от
# математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?

# task 5
def stats_5():
    
    # constants
    avg = 178
    std = math.sqrt(25)

    # calculate z-score
    z_score = st.NormalDist(avg, std).zscore(190)

    # print out result
    print('task_5:')
    print(f'z_score: {z_score}\n')

stats_5()