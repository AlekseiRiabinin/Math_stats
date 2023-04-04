# import math library
import math
import numpy as np 

# 1) Даны значения зарплат из выборки выпускников.
# Посчитать среднее арифметическое, среднее квадратичное отклонение, 
# смещенную и несмещенную оценки дисперсий для данной выборки.

# task 1
def stats():
    # given array
    arr = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])

    arr_mean = np.mean(arr) # average
    arr_std = np.std(arr) # standard deviation
    arr_var0 = np.var(arr, ddof=0) # variance (Delta Degrees of Freedom = 0)
    arr_var1 = np.var(arr, ddof=1) # variance (Delta Degrees of Freedom = 1)

    # print out results
    print('\ntask_1:')
    print(f'mean: {arr_mean}\nstd: {arr_std}\nvar (ddof=0): {arr_var0}\nvar (ddof=1): {arr_var1}\n')
    
stats()


# 2) В первом ящике находится 8 мячей, из которых 5 - белые. 
# Во втором ящике - 12 мячей, из которых 5 белых. 
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4 мяча. 
# Какова вероятность того, что 3 мяча белые?

'''
P1 = {event_space_1} / {sample_space_1} - вероятность вытащить 2 белых мяча из 1 ящика 
Применяется формула "combinations", поскольку n>k и порядок не важен.

- {event_space_1} для комбинаций из 2 мячей в 5 белых (1 ящик)
k=2 (извлеченные мячи из 1 ящика), n=5 (число белых мячей в 1 ящике)
- {sample_space_1} для комбинаций из 5 белых мячей среди всех в 1 ящике
k=5 (5 белых мячей), n=8 (общее число мячей в 1 ящике)

-----------------------------------------------------------------------------------------

P2 = {event_space_2} / {sample_space_2} - вероятность вытащить 4 белых мяча из 2 ящика
Применяется формула "combinations", поскольку n>k и порядок не важен.

- {event_space_2} для комбинаций из 4 мячей в 5 белых (2 ящик)
k=4 (извлеченные мячи из 2 ящика), n=5 (число белых мячей во 2 ящике)
- {sample_space_2} для комбинаций из 5 белых мячей среди всех во 2 ящике
k=5 (5 белых мячей), n=12 (общее число мячей во 2 ящике)

-----------------------------------------------------------------------------------------

P12 = P1 * P2 - вероятность вытащить белые мячи одновременно из 2-x ящиков (AND operator)

-----------------------------------------------------------------------------------------

P3 = 3 / (5 + 5) - вероятность вытащить 3 белых мяча из всех белых в 2-x ящиках

-----------------------------------------------------------------------------------------

P = P12 * P3 - вероятность вытащить 3 белых мяча при условии что из первого ящика 
вытаскивают случайным образом два мяча, из второго - 4 мяча.

'''

# task 2
def prob_2():

    # probability for the 1st box
    prob_1 = math.comb(5, 2) / math.comb(8, 5)

    # probability for the 2nd box
    prob_2 = math.comb(5, 4) / math.comb(12, 5)

    # probabilities for both boxes (AND operator)
    prob_12 = prob_1 * prob_2
    prob_3 = 3 / (5 + 5)

    # result (AND operator)
    P = prob_12 * prob_3
    
    # print out result
    print(f'task_2: {P}\n')            

prob_2()


# 3) На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. 
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. 
# Найти вероятность того, что выстрел произведен: 
# a) первым спортсменом 
# b) вторым спортсменом 
# c) третьим спортсменом

'''
P1 = 0.9
P2 = 0.8
P3 = 0.6

P123 = P1 + P2 + P3 - вероятность попадания или 1 или 2 или 3 спортсмена
(т.к один из трех стреляет)

P1_shoot = P1 * P123 - вероятность выстрела 1 спортсмена при условии что попал один из 3-x 
P2_shoot = P2 * P123 - вероятность выстрела 2 спортсмена при условии что попал один из 3-x 
P3_shoot = P3 * P123 - вероятность выстрела 3 спортсмена при условии что попал один из 3-x 
'''

# task 3
def prob_3():

    P1 = 0.9 # probability for 1st athlet to hit
    P2 = 0.8 # probability for 2nd athlet to hit
    P3 = 0.6 # probability for 3rd athlet to hit

    # probability that 1st athlet shot given probability of all athlets to hit
    P1_shoot = P1 * (P1 + P2 + P3)
   
    # probability that 2nd athlet shot given probability of all athlets to hit
    P2_shoot = P2 * (P1 + P2 + P3)

    # probability that 3rd athlet shot given probability of all athlets to hit
    P3_shoot = P3 * (P1 + P2 + P3)

    # print out results
    print('task_3:')
    print(f'1st athlet: {P1_shoot}\n2nd athlet: {P2_shoot}\n3rd athlet: {P3_shoot}\n')

prob_3()


# 4) В университет на факультеты A и B поступило равное количество студентов, 
# а на факультет C студентов поступило столько же, сколько на A и B вместе. 
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. 
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. 
# Студент сдал первую сессию. Какова вероятность, что он учится: 
# a) на факультете A 
# b) на факультете B 
# c) на факультете C

'''
x_A = 1/4 - Кол-во студентов на фак.A
x_B = 1/4 - Кол-во студентов на фак.B
x_c = 1/2 - Кол-во студентов на фак.C

p_A = 0.8 - Вероятность сдать на фак.A
p_B = 0.7 - Вероятность сдать на фак.B
p_C = 0.9 - Вероятность сдать на фак.C

E[X] = x_A * p_A + x_B * p_B + x_C * p_C - expectation (мат. ожидание)

pass_A = x_A * p_A - вероятность сдать на фак.A при данном кол-во студентов
pass_B = x_B * p_B - вероятность сдать на фак.B при данном кол-во студентов
pass_C = x_C * p_C - вероятность сдать на фак.C при данном кол-во студентов

prob_A = x_A / E - вероятность что студент учиться на фак.A
prob_B = x_B / E - вероятность что студент учиться на фак.B
prob_C = x_C / E - вероятность что студент учиться на фак.C
'''

# task 4
def prob_4():

    # number of students
    x_A = 1/4
    x_B = 1/4
    x_C = 1/2

    # probability to pass
    p_A = 0.8
    p_B = 0.7
    p_C = 0.9
    
    # expectation (weighted average)
    E = x_A * p_A + x_B * p_B + x_C * p_C
    
    # probability to pass given number of students
    pass_a = x_A * p_A
    pass_b = x_B * p_B
    pass_c = x_C * p_C

    # probability that a student studies at school
    prob_a = x_A / E
    prob_b = x_B / E
    prob_c = x_C / E

    # print out results
    print('task_4:')
    print(f'(a): {prob_a}\n(b): {prob_b}\n(c): {prob_c}\n')

prob_4()


# 5) Устройство состоит из трех деталей. 
# Для 1-й детали вероятность выйти из строя в первый месяц равна 0.1, для 2-й - 0.2, для 3-й - 0.25. 
# Какова вероятность того, что в первый месяц выйдут из строя: 
# a) все детали 
# b) только две детали 
# c) хотя бы одна деталь 
# d) от одной до двух деталей

'''
P1 = 0.1
P2 = 0.2
P3 = 0.25

a) выйдут из строя все (3) детали (оператор AND)
prob_a = P1 * P2 * P3

b) выйдут из только 2 детали при условии работы остальной ((1 - P) - деталь работает)
P23 = (1 - P1) * P2 * P3 - вероятность что выйдут из строя 2 и 3 детали
P13 = (1 - P2) * P1 * P3 - вероятность что выйдут из строя 1 и 3 детали
P12 = (1 - P3) * P1 * P2 - вероятность что выйдут из строя 1 и 2 детали
prob_b = P12 + P13 + P23

c) выйдет из строя 1 или 2 или 3 детали (оператор OR)
P33 = (1 - P1) * (1 - P2) * P3 - вероятность что выйдет из строя 3 деталь при условии работы 1 и 2
P22 = (1 - P1) * (1 - P3) * P2 - вероятность что выйдет из строя 2 деталь при условии работы 1 и 3
P11 = (1 - P2) * (1 - P3) * P1 - вероятность что выйдет из строя 1 деталь при условии работы 2 и 3
prob_1 = P11 + P22 + P33 - вероятность что выйдет из строя одна из трех деталей при условии работы остальных
prob_c = prob_a + prob_b + prob_1

d) выйдет из строя 1 или 2 детали (оператор OR)
prob_d = prob_b + prob_1
'''

# task 5
def prob_5():

    P1 = 0.1 # probability for 1st part to be out of order
    P2 = 0.2 # probability for 2nd part to be out of order
    P3 = 0.25 # probability for 3rd part to be out of order

    # probability that 3 parts are out of order
    prob_a = P1 * P2 * P3
   
    # probability that 2 parts are out of order given one is valid
    P23 = (1 - P1) * P2 * P3
    P13 = (1 - P2) * P1 * P3
    P12 = (1 - P3) * P1 * P2
    prob_b = P12 + P13 + P23

    # probability that 1 OR 2 OR 3 parts are out of order
    P33 = (1 - P1) * (1 - P2) * P3
    P22 = (1 - P1) * (1 - P3) * P2
    P11 = (1 - P2) * (1 - P3) * P1
    prob_1 = P11 + P22 + P33
    prob_c = prob_a + prob_b + prob_1

    # probability that 1 OR 2 parts are out of order
    prob_d = prob_b + prob_1

    # print out results
    print('task_5:')
    print(f'(a): {prob_a}\n(b): {prob_b}\n(c): {prob_c}\n(d): {prob_d}\n')

prob_5()