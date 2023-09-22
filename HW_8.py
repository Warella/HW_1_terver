import numpy as np
import scipy.stats as stats
from statsmodels.stats.weightstats import _tconfint_generic as t_stat

# Задача 1. Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks): 
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
# Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy 
# Полученные значения должны быть равны. 
# Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков, 
# а затем с использованием функций из библиотек numpy и pandas.

m_zp = zp.mean()
m_ks = ks.mean()
m_zpks = (zp * ks).mean()
cov = m_zpks - m_zp * m_ks
print(cov)
print(np.cov(zp, ks, ddof=0))

corr = cov / (np.std(zp)* np.std(ks))
print(corr)
print(np.corrcoef(zp, ks))

# Задача 2. Измерены значения IQ выборки студентов, обучающихся в местных технических вузах: 
iq = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111]) 
# Известно, что в генеральной совокупности IQ распределен нормально. 
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

mean_iq = iq.mean()
sigma_iq = iq.std(ddof=1)
alpha = 0.05
n_iq = len(iq)
mean_std_iq = sigma_iq / (np.sqrt(n_iq))

x1 = mean_iq + stats.t.ppf(sigma_iq/2, df= n_iq - 1) * sigma_iq/np.sqrt(n_iq)
x2 = mean_iq - stats.t.ppf(sigma_iq/2, df= n_iq - 1) * sigma_iq/np.sqrt(n_iq)
print((round(x1, 3), round(x2, 3)))

print(t_stat(mean_iq, mean_std_iq, n_iq - 1, alpha, 'two-sided'))

# Задача 3. Известно, что рост футболистов в сборной распределен нормально с дисперсией генеральной совокупности, равной 25 кв.см. 
# Объем выборки равен 27, среднее выборочное составляет 174.2. 
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

sigma = np.sqrt(25)
n = 27
mean = 174.2
alpha = 0.05
mean_std = sigma / (np.sqrt(n_iq))

x1 = mean + stats.t.ppf(sigma/2, df= n - 1) * sigma/np.sqrt(n)
x2 = mean - stats.t.ppf(sigma/2, df= n - 1) * sigma/np.sqrt(n)
print((round(x1, 3), round(x2, 3)))

print(t_stat(mean, mean_std, n - 1, alpha, 'two-sided'))