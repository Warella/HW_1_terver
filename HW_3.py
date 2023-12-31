# Задача 1. Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
# Посчитать (желательно без использования статистических методов наподобие std, var, mean):
# среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.

import numpy as np
x = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
averrage = np.mean(x)
std1 = np.std(x)
std2 = np.std(x, ddof=1)
sqrt1 = np.sqrt(np.var(x))
sqrt2 = np.sqrt(np.var(x, ddof=1))
result = ([averrage, std1, std2, sqrt1, sqrt2])
print(result)


import math
from math import factorial

# Задам функцию, которая будет считать по формуле сочетаний (без повторений)

def combination(k, n):
    return math.factorial(n) / math.factorial(k) / math.factorial(n - k)

# Задам функцию для биномиального распределения 

def binomial(k, n, p, q):
    return combination(k, n) * pow(p, k) * pow(q, n - k)

# Задам функцию для распределения Пуассона

def puasson(n, p, m):
    return pow(n * p, m) / factorial(m) * pow(2.72, -n * p)

# Задача 2. В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых. 
# Из первого ящика вытаскивают случайным образом 2 мяча, из второго - 4 мяча. Какова вероятность того, что 3 мяча белые?

result = combination(2, 5) * combination(0, 3) / combination(2, 8) * combination(1, 5) * combination(3, 7) / combination(4, 12) + \
    combination(1, 5) * combination(1, 3) / combination(2, 8) * combination(2, 5) * combination(2, 7) / combination(4, 12) + \
    combination(0, 5) * combination(2, 3) / combination(2, 8) * combination(3, 5) * combination(0, 7) / combination(4, 12)
print(round(result, 3))

# Задача 3. На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. 
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. 
# Найти вероятность того, что выстрел произведен: a). первым спортсменом 

result = 1/3 * 0.9 / (1/3 * 0.9 + 1/3 * 0.8 + 1/3 * 0.6)
print(round(result, 3))

# б). вторым спортсменом 

result = 1/3 * 0.8 / (1/3 * 0.9 + 1/3 * 0.8 + 1/3 * 0.6)
print(round(result, 3))

# в). третьим спортсменом.

result = 1/3 * 0.6 / (1/3 * 0.9 + 1/3 * 0.8 + 1/3 * 0.6)
print(round(result, 3))

# Задача 4. В университет на факультеты A и B поступило равное количество студентов, 
# а на факультет C студентов поступило столько же, сколько на A и B вместе. 
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. 
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. 
# Студент сдал первую сессию. Какова вероятность, что он учится: a). на факультете A 

result = (1/4 * 0.8) / (1/4 * 0.8 + 1/4 * 0.7 + 1/2 * 0.9)
print(round(result, 3))

# б). на факультете B 

result = (1/4 * 0.7) / (1/4 * 0.8 + 1/4 * 0.7 + 1/2 * 0.9)
print(round(result, 3))

# в). на факультете C?

result = (1/4 * 0.9) / (1/4 * 0.8 + 1/4 * 0.7 + 1/2 * 0.9)
print(round(result, 3))

# Задача 5. Устройство состоит из трех деталей. 
# Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25. 
# Какова вероятность того, что в первый месяц выйдут из строя: а). все детали 

result = 1/3 * 0.1 * 1/3 * 0.2 * 1/3 * 0.25
print(round(result, 3))

# б). только две детали 

result = 1/3 * 0.1 * 1/3 * 0.2 + 1/3 * 0.1 * 1/3 * 0.25 + 1/3 * 0.2 * 1/3 * 0.25
print(round(result, 3))

# в). хотя бы одна деталь 

result = 1 - 1/3 * 0.9 * 1/3 * 0.8 * 1/3 * 0.75
print(round(result, 3))

# г). от одной до двух деталей?

result = 1/3 * 0.1 + 1/3 * 0.2 + 1/3 * 0.25 + 1/3 * 0.1 * 1/3 * 0.2 + 1/3 * 0.1 * 1/3 * 0.25 + 1/3 * 0.2 * 1/3 * 0.25
print(round(result, 3))