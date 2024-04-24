from polynomial import Polynomial
import matplotlib.pyplot as plt
import math
import numpy as np
import scipy.integrate as integrate
from Qn5 import chebyshev

def ortho():
    polys = []
    for i in range(1,6):
        polys.append(chebyshev(i))
    w = lambda x : 1/(math.sqrt(1-x**2))
    for i in range(0,5):
        for j in range(0,5):
            f  = lambda x : ((polys[i]*polys[j])[x] )/ math.sqrt(1-x**2)
            if i==j:
                c,_ = integrate.quad(f,-1,1)
                if c<=0:
                    return 0
            else :
                c,_ = integrate.quad(f,-1,1)
                # print(round(c,2))
                # c = round(c,2)
                if round(c,2)>0:
                    print("hi")
                    return 0
                
    return 1

if __name__=="__main__":
    c = ortho()
    print(c)

# def ChebyshevVarify ():
#     n = 5
#     print("j\i",end="")
#     for i in range(1,n+1):
#         print("\t"+str(i),end="")
#     print("\n ",end="")
#     for i in range(1,n+1):
#         print("--------",end="")
#     print("--")


#     for i in range(1,n+1):
#         print(i, end="|\t")
#         Chi = ChebyshevPolynomial(i)
#         for j in range(1,i+1):
#             Chj = ChebyshevPolynomial(j)
#             f = lambda x : ((Chi*Chj)[x])/sqrt(1-x**2)
#             integral , error = quad(f,-1,1)
#             print(round(integral,2),end="\t")
#         print()
    
#     print("NOTE: The ith column and jth row represents the integral value of Ti-1 and Tj-1 with the given weight in the range [-1,1]")

# if __name__ == "__main__":
    
#     ChebyshevVarify()