import matplotlib.pyplot as plt
import numpy as np
from math import sin

import datetime
import time

"""
Пример функции: y=t*t + 2/t, где
t - unixtime в интервале [datetime.now() - interval, datetime.now()] с шагом dt,
Interval - глубина периода моделирования в днях
datetime.now() - дата обработки
dt - шаг в часах
"""
date_now = datetime.datetime.now()
interval = int(input())
dt = int(input())
start = date_now - datetime.timedelta(days=interval)

x_axe = [start + datetime.timedelta(days=i * dt) for i in range((interval // dt) + 1)]
x_axe_unix = list(map(datetime.datetime.timetuple, x_axe))
print(x_axe_unix)

x_axe_unix = list(map(time.mktime, x_axe_unix))

print(x_axe_unix)

func = lambda x: 1 if sin(x) >= 0 else 0
y_axe = list(map(func, x_axe_unix))
fig, ax = plt.subplots()
ax.plot(x_axe_unix, y_axe)
plt.show()
print(ax)