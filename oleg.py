import matplotlib.pyplot as plt
from scipy.special import legendre
import numpy as np

def leg(x):
    return legendre(x)
summ = 0
for i in range(1, 16, 2):
    summ += legendre(i) * np.exp(-i / 10)
x = np.linspace(-1,1,1000)

plt.scatter(-1,summ(-1), label = f'Минимум функции = {summ(-1)} ')
plt.plot(x,summ(x))
plt.scatter(-0.5,summ(-0.5), color = 'red', label = f'Минимум функции при х = -0.5  равен {summ(-0.5)}')
plt.scatter(0.5,summ(0.5), color = 'red',label = f'Минимум функции при х = 0.5  равен {summ(0.5)}')
plt.grid()
plt.legend()
plt.show()