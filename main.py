# 1. Определить корни
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# 4. Постоить график
# 5. Вычислить вершину
# 6. Определить промежутки, на которых f > 0
# 7. Определить промежутки, на которых f < 0

import numpy as np
import matplotlib.pyplot as plt

list = [-12, -18, 5, 10, -30]
x_limit=[-100, 100]
x=np.arange(x_limit[0], x_limit[1], 0.1)

def func(x, a, b, c, d, e):
    return a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e

x_change=[]
func_direct=-1

color = 'r'
def change_color():
    global color
    if color == "r":
        color = "b"
    else:
        color = "r"
    return color

for i in range(len(x)-1):
    if func_direct == -1:
        if func(x[i], *list) < func(x[i+1], *list):
            x_change.append((x[i], func(x[i], *list)))
            func_direct = 1
    else:
        if func(x[i], *list) > func(x[i+1], *list):
            x_change.append((x[i], func(x[i], *list)))
            func_direct = -1

def roots(x, list_roots):
    for i in x:
        if (func(i, *list) > 0 and func(i-0.01, *list) < 0) or (func(i, *list) < 0 and func(i-0.01, *list) > 0):
            list_roots.append(round(i, 4))
    return list_roots
list_roots = []
roots(x, list_roots)
print("Корни функции:", (list_roots))


x_range = np.arange(x_limit[0], x_change[0][0], 0.1)
plt.plot(x_range, func(x_range, *list), change_color())
for i in range(len(x_change)-1):
    x_range = np.arange(x_change[i][0], x_change[i+1][0], 0.1)
    plt.plot(x_range, func(x_range, *list), change_color())
x_range = np.arange(x_change[len(x_change)-1][0], x_limit[1], 0.1)
plt.plot(x_range, func(x_range, *list), change_color())

plt.xlabel('Ось Х')
plt.ylabel('Ось Y')
plt.grid()
plt.show()
