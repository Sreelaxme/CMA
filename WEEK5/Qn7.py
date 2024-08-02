from numpy import e ,pi,sin,cos
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
f = lambda x : e**x

def S(a0,ai,bi, n,x):
    y = a0
    for i in range(1,n+1):
        y+= ai[i]*cos(i*x)+bi[i]*sin((i)*x)

    # for i in range(n):
    #     y+=bi[i]*sin((i+1)*x)

    return y
    
def fourier(n):
    ai = []
    bi = [0]
    for i in range(n+1):
        a,_ = quad(lambda x : f(x)*cos(i*x), -pi,pi)
        a = a/pi
        ai.append(a)
    for i in range(1,n+1):
        b ,_= quad(lambda x : f(x)*sin(i*x),-pi,pi)
        b = b/pi
        bi.append(b)

    a0 = ai[0]/2
    X = np.linspace(-pi,pi,100)
    Y = f(X)
    plt.plot(X,Y,label = 'actual',color = 'green')
    s = S(a0,ai,bi,n,X)
    plt.plot(X,s,label = 'fourier',color = 'red')
    plt.legend()
    plt.show()

if __name__ == "__main__":

    fourier(50)