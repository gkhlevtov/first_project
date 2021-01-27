import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

aluminum = [920, 660, 390000] # C, tпл, λ
iron = [460, 1539, 213000]
tin = [230, 232, 61000]
metals = [aluminum, iron, tin]

sp_metals = ['aluminum','iron','tin']
print('Металлы на выбор:', *sp_metals)

metal = metals[int(input('Введите номер металла от 1 до 3: '))-1]
mass = int(input('Введите массу металла: '))
power = int(input('Введите мощность печи в Вт: '))
t_start = int(input('Введите начальную температуру в градусах Цельсия: '))

print('', '----------------------------', '----------------------------', '----------------------------', '', sep="\n")
Q_1 = metal[0] * (metal[1] - t_start) * mass
time_1 = Q_1 / power
time_2 = (metal[2] * mass) / power

time = time_1 + time_2

print(time_1, 'время нагрева')
print(time_2, 'время плавки')
print(time, 'Общее время')

time_sp = []
for i in range(math.floor(time)):
    time_sp.append(i)

d_t = Q_1 / (metal[0] * mass)
d_t_s = d_t / time_1
print(d_t, 'общее изменение t')
print(d_t_s, 'изменение t в секунду')

t_1_sp = []
a = t_start

for i in range(math.floor(time_1)):
    a += d_t_s
    t_1_sp.append(a)

t_2_sp = []
tt = metal[1]

for i in range(math.ceil(time_2)):
    t_2_sp.append(tt)

t_sp = t_1_sp + t_2_sp

g_title = 'График плавления '
if metal == aluminum:
    g_title += 'алюминия'
elif metal == iron:
    g_title += 'железа'
elif g_title == tin:
    g_title += 'олова'
    
   
plt.title(g_title) # Задаем название графика
plt.xlabel('Время, с') # Задаем название оси X
plt.ylabel('Температура, °C') # Задаем название оси X

plt.plot(time_sp, t_sp, c='r', linewidth=2)
plt.show()
