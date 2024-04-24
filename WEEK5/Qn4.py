from polynomial import Polynomial
import matplotlib.pyplot as plt
import math
import numpy as np
import scipy.integrate as integrate

def f(x):
    return (math.e)**x
def legendre(n):
    P = Polynomial([1])
    for i in range(n):
        x = Polynomial([-1,0,1])
        P = P*x
    
    for i in range(n):
        P = P.derivative()

    legendre = 1/(2**(n) * math.factorial(n))*P

    return legendre

def leastSq(n):
    a = -1
    b = 1
    ai = []
    for j in range(n+1):
        lp = legendre(j)
        cj,_ = integrate.quad(lambda x : (lp*lp)[x],a,b)
        aj,_ =  (integrate.quad(lambda x :lp[x] * f(x),a,b))
        aj = aj/cj
        ai.append(aj)

    p = Polynomial([0])

    for i in range(n+1):
        p = p + ai[i]*legendre(i)

    X = np.linspace(-1,1,100)
    Y = f(X)
    plt.plot(X,Y,label = 'True', color = 'green')
    p.show(-1,1)
    plt.show()
    return p

if __name__ == "__main__":
    p = leastSq(4)
    print(p)