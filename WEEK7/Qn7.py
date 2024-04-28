from polynomial import Polynomial
import random
import numpy as np
import scipy.integrate as integrate 
import matplotlib.pyplot as plt
def poly(n, f,M,plot = False, a = 0, b = np.pi):
    
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
        x_coords = np.linspace(a,b,M)
        y_coords = f(x_coords)
        plt.plot(x_coords,y_coords,label = 'True', color= 'red')
        plt.show()
    return P

def roots (f,a,b):
    M = int((b-a)*100)
    x_prev = a
    X0 = []
    for x in np.linspace(a,b,M):
        if f(x_prev) * f(x) <= 0:
            X0.append(x)
        x_prev = x

    P = poly(len(X0)+5,f,M,a=a,b=b)
    return P.printRoots(X0)


if __name__ == '__main__':


    print("x³ - 6x² + 11x - 6")
    print("Intervel [-5, 5]")
    f = lambda x: x**3 - 6*x**2 + 11*x - 6
    X = roots(f, -5, 5)
    X_actual = [1, 2, 3]
    print("calculated roots :", X)
    print("actual roots:", X_actual)
    print("f(X): ", [f(x) for x in X])