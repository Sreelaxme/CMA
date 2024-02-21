import math
from math import sqrt,pi ,e ,log
import numpy as np
import matplotlib.pyplot as plt

def stirling(n):
    return sqrt(2*pi*n) * ((n/e)**n)

def stirlingLog(n):
    return 0.5*math.log(2*math.pi*n) + n*math.log(n/math.e)
def factorial(n):
    if n==1:
        return n
    return n*factorial(n-1)

def factorialLog(n):
    fact = 0
    while n>1:
        fact += log(n)
        n-=1

    return fact

def factLogList(n):
    fact = 0
    factList = []

    for i in range(1,n):
        fact += log(i)
        factList.append(fact)

    return factList

if __name__ == "__main__":
    n = 1000000

    n_values = list(range(1,n))

    stirlingValues = [stirlingLog(i) for i in n_values]

    factValues = factLogList(n)

    plt.plot(n_values,stirlingValues,label = 'Stirling')
    plt.plot(n_values,factValues,label = 'Log of actual values')
    plt.title("Stirling log vs factorial log")
    plt.legend()
    plt.grid()
    plt.show()