from polynomial import Polynomial
import matplotlib.pyplot as plt
import math
import numpy as np
import scipy.integrate as integrate

    

def chebyshev(n):
    if n==1:
        return Polynomial([1])
    if n==2:
        return Polynomial([0,1])
    return 2*Polynomial([0,1])*chebyshev(n-1) - chebyshev(n-2)

if __name__ == "__main__":
    c = chebyshev(3)
    print(c)