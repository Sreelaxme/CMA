from math import e
import numpy as np
import matplotlib.pyplot as plt

def f_x(x):
  return 2 * x * e**(x ** 2)

def integral(a,b):
  return e**(b ** 2) - e**(a ** 2)

def trapizoidal_integral(f, a, b, M):
    """
    Function that calculates, using trapizoidal approximation, the definite integral of function f in limits a and b, using M intervals.
    """
    return sum([f(a + i*(b-a)/M) + f(a + (i+1)*(b-a)/M) for i in range(M)])*(b-a)/(2*M)

Ms = list(range(100,1000))
trapezoidal = [trapizoidal_integral(f_x, 1, 3, M) for M in Ms]

true_area = integral(1,3)

plt.plot(Ms, trapezoidal , label ='Area using Trapezoidal method')
plt.axhline(true_area, label = 'Area using integral', color = 'r')

plt.xlabel('M')
plt.ylabel('Area')
plt.legend()
plt.show()
