import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, romberg, simpson
from numpy import e

def f_x(x):
    return 2 * x * e**(x ** 2)

def integral(a, b):
    return e**(b ** 2) - e**(a ** 2)

def areas(u):
    x = np.linspace(0, u)
    ys = [f_x(i) for i in x]
    resultq, error = quad(f_x, 0, u)
    resultr = romberg(f_x, 0, u)
    results = simpson(ys, x)
    return resultq, resultr, results



quad_result = []
romberg_result = []
simpson_result = []
true_area = []
u = np.linspace(0, 1, 50)

for i in u:
    rq, rr, rs = areas(i)
    romberg_result.append(rr)
    quad_result.append(rq)
    simpson_result.append(rs)
    true_area.append(integral( 0,i))

plt.plot(u, quad_result, label='Area using quad method')
plt.plot(u, romberg_result, label='Area using romberg method')
plt.plot(u, simpson_result, label='Area using simpson method')

plt.plot(u, true_area, label='Area using integral', color='r')

plt.xlabel('u')
plt.ylabel('Area')
plt.title('Comparison of Integration Methods')
plt.legend()
plt.grid(True)
plt.show()