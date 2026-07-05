import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. Параметры орбиты
t = np.linspace(0, 2*np.pi, 100)
e = 0.5
r = 1 / (1 + e * np.cos(t))

x = r * np.cos(t)
y = r * np.sin(t)

# 2. Рисуем картинку
fig = plt.figure(figsize=(8, 8))
ax = plt.axes()

# Настройки внешнего вида
ax.set_facecolor('black')
ax.set_title('Модель движения планеты по эллиптической орбите', color='white')
ax.grid(color='gray', linestyle='--', linewidth=0.5)  # <--- ВСЯ МАГИЯ ЗДЕСЬ

# Рисуем Солнце
ax.scatter(0, 0, color='yellow', s=500, edgecolors='orange', linewidth=2)

# Рисуем орбиту
ax.plot(x, y, color='cyan', linewidth=1.5)

# Заготовка для планеты
point, = ax.plot([], [], 'bo', markersize=12)

# 3. Анимация
def update(frame):
    i = frame % len(x)
    point.set_data([x[i]], [y[i]])
    return point,

ani = animation.FuncAnimation(fig, update, frames=200, interval=50)

plt.show()
