from Qn1 import Matrix
import math
import numpy as np


def qreig(M:Matrix):
    A = Matrix(M.m,M.n)
    
    A.matrix = M.matrix
    max_iter = 1000
    Qs = Matrix
    for _ in range(max_iter):
        Q,R = np.linalg.qr(A.matrix)
        A.matrix = np.dot(R,Q)
    eigenvalues = []
    for i in range(A.m):
        eigenvalues.append(A[i,i])
    # return eigenvalues

    eigenvectors = []
    I = Matrix(A.m,A.n)
    I.toEye()
    for eig in eigenvalues:
        # Mc = Matrix(M.m,M.n)
        # Mc.matrix = M.matrix
        X = A - eig*I
        
        # X.solvezero()
        eigenvectors.append((X.solvezero()).matrix)

    return eigenvalues,eigenvectors

Matrix.qreig = qreig

if __name__=="__main__":
    m = Matrix(4, 4)
    m.randomize()
    m = m + m.t()
    e, v = m.qreig()
    print(e)
    print(v) # v[:,i] is the eigenvector for eigenvalue e[i,0]
    print(np.linalg.eig(m.matrix))
    