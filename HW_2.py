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

# Задача 1. Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. 
# Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.

print(round(binomial(85, 100, 0.8, 0.2), 3))

# Задача 2. Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. 
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек. 
# Какова вероятность, что ни одна из них не перегорит в первый день? 

print(round(puasson(5000, 0.0004, 0), 3))

# Какова вероятность, что перегорят ровно две?

print(round(puasson(5000, 0.0004, 2), 3))

# Задача 3. Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

print(round(binomial(70, 144, 0.5, 0.5), 3))

# Задача 4. В первом ящике находится 10 мячей, из которых 7 - белые. 
# Во втором ящике - 11 мячей, из которых 9 белых. 
# Из каждого ящика вытаскивают случайным образом по два мяча. 
# Какова вероятность того, что все мячи белые? 

result = combination(2, 7) * combination(0, 3) / combination(2, 10) * combination(2, 9) * combination(0, 2) / combination(2, 11)
print(round(result, 3))

# Какова вероятность того, что ровно два мяча белые? 

result = combination(2, 7) * combination(0, 3) / combination(2, 10) * combination(0, 9) * combination(2, 2) / combination(2, 11) + \
    combination(0, 7) * combination(2, 3) / combination(2, 10) * combination(2, 9) * combination(0, 2) / combination(2, 11) + (
    combination(1, 7) * combination(1, 3) / combination(2, 10) * combination(1, 9) * combination(1, 2) / combination (2, 11))
print(round(result, 3))

# Какова вероятность того, что хотя бы один мяч белый?

result = 1 - combination(0, 7) * combination(2, 3) / combination(2, 10) * combination(0, 9) * combination(2, 2) / combination(2, 11)
print(round(result, 3))