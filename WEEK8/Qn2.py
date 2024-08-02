import numpy as np
import random 
import math
from Qn1 import Matrix

def deflate(A:Matrix):
    n = A.n
    # E = Matrix(n,1)
    # V = Matrix(n,n)
    E = list()
    V = list()
    for i in range(n):
        print("hehe")
        e,v = A.Power(A)

        # print(e)
        # E[i,0] = e 
        e = e[0,0]
        E.append(e)
        V.append(v)
        print("done?")
        # for j in range(n):


        #     V[i,j] = v[i,0]
        A = A - e*np.dot(v,v.t())

    return E,V


Matrix.deflate = deflate

if __name__=="__main__":
    m = Matrix(4, 4)
    m.randomize()
    m = m + m.t()
    e, v = m.deflate()
    print(e)
    print(v) 
    print(np.linalg.eig(m.matrix))
    