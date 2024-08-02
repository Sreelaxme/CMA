from polynomial import Polynomial
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
import math

def f(x):
    return np.sin(x) + np.cos(x)

def poly(n):
    a = 0
    b = np.pi
    A = []
    B = []
    for j in range(n+1):
        temp,_ = integrate.quad(lambda x : x**j * f(x),a,b)
        coeff = []
        for k in range(n+1):
            sum,_ = integrate.quad(lambda x: x**(j+k),a,b)
            coeff.append(sum)

        A.append(coeff)
        B.append(temp)

    X = np.linalg.solve(A,B)
    P = Polynomial([0])
    P.coeff = np.array([float(i) for i in X])
    P.show(a,b)
    x_coords = np.linspace(a,b,100)
    y_coords = f(x_coords)
    plt.plot(x_coords,y_coords,label = 'True', color= 'red')
    plt.show()

if __name__ =='__main__':

    poly(3)