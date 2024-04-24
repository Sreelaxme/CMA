from polynomial import Polynomial
import matplotlib.pyplot as plt
import math

def legendre(n):
    P = Polynomial([1])
    for i in range(n):
        x = Polynomial([-1,0,1])
        P = P*x
    
    for i in range(n):
        P = P.derivative()

    legendre = 1/(2**(n) * math.factorial(n))*P

    return legendre

if __name__ == "__main__":
    p = legendre(1)
    print(p)

