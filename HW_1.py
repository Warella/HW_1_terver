import math
from math import factorial

# Задам функцию, которая будет считать по формуле сочетаний (без повторений)

def combination(k, n):
    return math.factorial(n) / math.factorial(k) / math.factorial(n - k)

# Задача 1. Из колоды в 52 карты извлекаются случайным образом 4 карты. 
# a) Найти вероятность того, что все 4 карты – крести. 

result = combination(4, 13) * combination(0, 39) / combination(4, 52)
print(round(result, 3))

# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

result = (combination(1, 4) * combination(3, 48) + combination(2, 4) * combination(2, 48) + combination(3, 4) * combination(1, 48) + combination(4, 4) * combination(0, 48)
) / combination(4, 52)
print(round(result, 3))

# Задача 2. На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. 
# Код содержит три цифры, которые нужно нажать одновременно . 
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

result = 1 / (10 * 9 * 8)
print(round(result, 3))

# Задача 3. В ящике имеется 15 деталей, из которых 9 окрашены. 
# Рабочий случайным образом извлекает 3 детали. 
# Какова вероятность того, что все 3 извлеченные детали окрашены?

result = combination(3, 9) * combination(0, 6) / combination(3, 15)
print(round(result, 3))

# Задача 4. В лотерее 100 билетов. 
# Из них 2 выигрышных. 
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

result = combination(2, 2) * combination(0, 98) / combination(2, 100)
print(round(result, 4))