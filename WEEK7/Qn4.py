import matplotlib.pyplot as plt
import math
import numpy as np

def newton_raphson(f,fdash,x0,e):
    x = x0
    x0 = x+10*e
    count = 0
    while abs(x-x0) > e :
        x,x0 = x - (f(x)/fdash(x)) , x 
        count+=1
    return x,count

def secant(f,x0,e):
    x = x0
    x0 = x+10*e
    count = 0
    while abs(x-x0)>e :
        x,x0 = x - (f(x)*(x-x0)/(f(x)-f(x0))), x
        count += 1
    return x, count


if __name__ == '__main__':
    import math

    ## Case 1
    f = lambda x: x**3 - 2*x + 2
    f_dash = lambda x: 3*x**2 - 2
    e = 0.001
    
    _,nr = newton_raphson(f,f_dash,-1,e)
    _,se = secant(f,-1,e)

    print(nr)
    print(se)
