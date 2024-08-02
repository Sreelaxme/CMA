import numpy as np
import math
import matplotlib.pyplot as plt
from math import e
f1 = lambda x : 3*x[0] - np.cos(x[1]*x[2]) - 1.5
f2 = lambda x : 4*(x[0]**2) - 625*(x[1]**2) + 2* x[2] - 1
f3 = lambda x : 20 * x[2] + np.e**(-x[0]*x[1]) + 9

f1_d1 = lambda x : 3
f2_d1 = lambda x : 8*x[0]
f3_d1 = lambda x : (-x[1]* np.e**(-x[0]*x[1]))

f1_d2 = lambda x : np.sin(x[1]*x[2]) * x[2]
f2_d2 = lambda x : -1250 * x[1]
f3_d2 = lambda x : (-x[0]* np.e**(-x[0]*x[1]))

f1_d3 = lambda x : np.sin(x[1]*x[2]) * x[1]
f2_d3 = lambda x : 2
f3_d3 = lambda x : 20 

f = lambda x : np.array([f1(x),f2(x),f3(x)])
def J(x):
    return [[f1_d1(x), f1_d2(x), f1_d3(x)],
            [f2_d1(x), f2_d2(x), f2_d3(x)],
            [f3_d1(x), f3_d2(x), f3_d3(x)]]


def newton_raphson(tol):
    x = np.array([1,1,1])
    x_old = np.array([0,0,0])
    mod_f = [np.linalg.norm(x)]
    while np.linalg.norm(x-x_old) > tol:
        x_old = x 
        x = x - np.linalg.inv(J(x))@f(x)
        mod = np.linalg.norm(x)
        mod_f.append(mod)

    return x,mod_f

def visualize(tol):
    x,mod_f = newton_raphson(tol)
    plt.plot(range(1,len(mod_f)+1),mod_f)
    plt.xlabel("iterations")
    plt.ylabel("norm")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    tolerance = 1e-6
    visualize(tolerance)