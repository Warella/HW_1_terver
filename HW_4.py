from math import sqrt
from scipy import stats
# Задача 1. Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800]. 
# Найдите ее среднее значение и дисперсию.
# a = 200, b = 800
result1 = (200 + 800) / 2
result2 = (800 - 200)**2 / 12
print("Среднее значение равно", result1, ", диспресия равна", result2)

# Задача 2. О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5? Если да, найдите ее.
# a = 0.5, D = 0.2
result1 = sqrt(0.2 * 12) + 0.5
result2 = (0.5 + result1) / 2
print("Среднее значение равно", round(result2, 2), ", правая граница равна", round(result1, 2))

# Задача 3. Непрерывная случайная величина X распределена нормально и задана плотностью распределения
# f(x) = (1 / (4 * sqrt(2pi))) * exp((-(x+2)**2) / 32)
# Найдите:
# а). M(X) = -2
# б). D(X) = 4*4 = 16
# в). std(X) (среднее квадратичное отклонение) = 4
print("Мат.ожидание равно -2, диперсия равна 16, среднее квадратическое отклонение равно 4")

# Задача 4. Рост взрослого населения города X имеет нормальное распределение, причем, средний рост равен 174 см, 
# а среднее квадратическое отклонение равно 8 см. посчитайте, какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
mu = 174
sigma = 8
# 1. больше 182 см?
x = 182
result = 1 - stats.norm.cdf((x - mu) / sigma)
print("1.", round(result, 2))
# 2. больше 190 см?
x = 190
result = 1 - stats.norm.cdf((x - mu) / sigma)
print("2.", round(result, 2))
# 3. от 166 см до 190 см?
x1 = 166
x2 = 190
result = stats.norm.cdf((x2 - mu) / sigma) - stats.norm.cdf((x1 - mu) / sigma)
print("3.", round(result, 2))
# 4. от 166 см до 182 см?
x1 = 166
x2 = 182
result = stats.norm.cdf((x2 - mu) / sigma) - stats.norm.cdf((x1 - mu) / sigma)
print("4.", round(result, 2))
# 5. от 158 см до 190 см?
x1 = 158
x2 = 190
result = stats.norm.cdf((x2 - mu) / sigma) - stats.norm.cdf((x1 - mu) / sigma)
print("5.", round(result, 2))
# 6. не выше 150 см или не ниже 190 см?
x1 = 150
x2 = 190
result = stats.norm.cdf((x1 - mu) / sigma) + 1 - stats.norm.cdf((x2 - mu) / sigma)
print("6.", round(result, 2))
# 7. не выше 150 см или не ниже 198 см?
x1 = 150
x2 = 198
result = stats.norm.cdf((x1 - mu) / sigma) + 1 - stats.norm.cdf((x2 - mu) / sigma)
print("7.", round(result, 2))
# 8. ниже 166 см?
x = 166
result = stats.norm.cdf((x - mu) / sigma)
print("8.", round(result, 2))

# Задача 5. На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см, от
# математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?
result = (190 - 178) / 5
print("Рост человека, равный 190 см, отклоняется на", result, "сигм")