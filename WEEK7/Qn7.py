from polynomial import Polynomial
import random
import numpy as np
import scipy.integrate as integrate 
import matplotlib.pyplot as plt
def poly(n, f,plot = False, a = 0, b = np.pi):
    
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
    if plot : 
        P.show(a,b)
        x_coords = np.linspace(a,b,100)
        y_coords = f(x_coords)
        plt.plot(x_coords,y_coords,label = 'True', color= 'red')
        plt.show()
    return P

def roots (f,a,b):
    M = int((b-a)*100)
    x_prev = a
    X0 = []
    