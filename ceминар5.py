import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import _tconfint_generic as t_stat
from scipy.stats import norm 
import math

# 3.Проведите тест гипотезы. 
# Продавец утверждает, что средний вес пачки печенья составляет 200 г.
# Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
# 202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
# Известно, что их веса распределены нормально.
# Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%?

X = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])
mean_X = X.mean()
std_X = X.std(ddof=1)
t_fact = (mean_X - 200) / std_X * np.sqrt(10)
print(t_fact)
t_cr = 3.25