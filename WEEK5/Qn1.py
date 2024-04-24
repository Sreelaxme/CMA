import matplotlib.pyplot as plt 
from polynomial import Polynomial
import numpy as np
#points array of tuples 
# best fit upto n 
def bestFit(points,n):
    A = []
    b = []
    for j in range(n+1):
        c = []
        for k in range(n+1):
            sum= 0
            for x,_ in points:
                sum += x**(j+k)
            c.append(sum)
        temp = 0
        for x,y in points:
            temp += y* (x**j)

        A.append(c)
        b.append(temp)
    X = np.linalg.solve(A,b)
    p = Polynomial([0])
    p.coeff = np.array([float(i) for i in X])


    x_coords = [point[0] for point in points ]
    y_coords = [point[1] for point in points ]
    p.show(min(x_coords),max(x_coords))
    plt.scatter(x_coords,y_coords)

    plt.grid(True)
    plt.show()
    
if __name__ == "__main__":
    bestFit(((0,1),(2,7),(1,3),(-1,1)),2)