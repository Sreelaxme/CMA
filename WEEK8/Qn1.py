import numpy as np
import random 
import math
class Matrix:
    def __init__(self,m,n):
        self.m = m
        self.n = n 
        self.matrix = np.zeros((m, n), dtype=float)
    
    def __setitem__(self,index,val):
        self.matrix[index[0]][index[1]] = val
    
    def __getitem__(self,index):
        return self.matrix[index[0]][index[1]]
    
    def __str__(self):
        mat = "A "+ str(self.m) +" x " + str(self.n) + " matrix with entries: \n"
        for i in range(self.m):
            for j in range(self.n):
                mat += '{:<10.8f}'.format(float(self.matrix[i][j]))
                mat += " "

            mat += "\n"

        return mat
    
    def toEye(self):
        for i in range(self.m):
            for j in range(self.n):
                if i==j:
                    self.matrix[i,j] =  1 
        
        # U, S, Vt = np.linalg.svd(self.matrix)
        # diagonal_matrix = np.diag(S)
        # transformation_matrix = U
        # print(transformation_matrix)
        # # self.matrix =  transformation_matrix
        # return transformation_matrix

    def toOne(self):
        for i in range(self.m):
            for j in range(self.n):
                self.matrix[i,j] =  1 

    def randomize(self):
        for i in range(self.m):
            for j in range(self.n):
                x = random.uniform(0,1)
                self.matrix[i,j] = x

    def t(self):
        m = self.n
        n = self.m
        newMatrix = Matrix(m,n)
        for i in range(self.m):
            for j in range(self.n):
                newMatrix[j,i] = self.matrix[i][j]

        return newMatrix
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        
        # Check if matrices have the same shape
        if self.m != other.m or self.n != other.n:
            return False
        
        # Compare elements element-wise
        return np.array_equal(self.matrix, other.matrix)
    def __ne__(self, other):
        return not self.__eq__(other)
    def __add__(self,mat):
        if mat.m!=self.m or mat.n!=self.n:
            raise Exception("Dimension incompatibility")
        else:
            newMatrix = Matrix(mat.m,mat.n)
            for i in range(self.m):
                for j in range(self.n):
                    newMatrix[i,j] = mat[i,j]+self.matrix[i,j]

        return newMatrix
    
    def __sub__(self,mat):
        if mat.m!=self.m or mat.n!=self.n:
            raise Exception("Dimension incompatibility")
        else:
            newMatrix = Matrix(mat.m,mat.n)
            for i in range(self.m):
                for j in range(self.n):
                    newMatrix[i,j] = -mat[i,j]+self.matrix[i,j]

        return newMatrix
    
    # def __mul__(self,mat):
    #     if isinstance(mat,Matrix):
    #         if self.n!=mat.m:
    #             raise Exception("Dimension incompatibility")
    #         else:
    #             newMatrix = Matrix(self.m,mat.n)
    #             for i in range(self.m):
    #                 for j in range(mat.n):
    #                     dot_product = 0
    #                     for k in range(self.n):
    #                         dot_product = self.matrix[i,k]*mat[k,j]
    #                     newMatrix[i,j] = dot_product

    #         return newMatrix
    #     elif isinstance(mat,(int,float)):
    #         newMatrix = Matrix(self.m,self.n)
    #         for i in range(self.m):
    #             for j in range(self.n):
    #                 newMatrix[i,j] = self.matrix[i][j]*mat
    #         return newMatrix
    #     else :
    #         raise Exception("Something is off")
    def __mul__(self,a):
        if(isinstance(a,Matrix)):
            if(a.m == self.n):
                m = Matrix(self.m,a.n)
                for i in range(self.m):
                    for j in range(a.n):
                        for k in range(a.m):
                            m[i,j] += self.matrix[i][k] * a[k,j]
                return m
            else: raise Exception("Invalid multiplication")
        elif(isinstance(a,(int,float))):
            m = Matrix(self.m,self.n)
            for i in range(self.m):
                for j in range(self.n):
                    m[i,j] = self.matrix[i][j]*a
            return m

    def __rmul__(self,mat):
        if isinstance(mat,(int,float)):
            newMatrix = Matrix(self.m,self.n)
            for i in range(self.m):
                for j in range(self.n):
                    newMatrix[i,j] = self.matrix[i][j]*mat
            return newMatrix
        else:
            raise Exception("Something off")
    def __truediv__(self, other):
        # if isinstance(other, Matrix):
        #     # Perform matrix division (right division)
        #     return np.linalg.solve(other.matrix.T, self.matrix.T).T
        if isinstance(other, (int, float)):
            # Perform scalar division
            return Matrix(self.m, self.n) + (1 / other) * self
        else:
            raise TypeError("Unsupported operand type for division")

    def norm (self,p,q=None):
        if q ==None:
            if p == math.inf:
                q = 1
            else :q = p
        
        sigma = 0
        for j in range(self.n):
            sum = 0
            for i in range(self.m):
                sum+=(self.matrix[i][j])**p
            
            sigma+=(sum**(q/p))
        
        return sigma**(1/q)
            
    def solvezero(self):
        Q,R = np.linalg.qr(self.matrix)
        n = self.n

        rank = np.linalg.matrix_rank(self.matrix)
        
        if rank<n:
            x = np.zeros(n)
            free_var_index = rank
            x[free_var_index] = 1
            for i in range(rank-1, -1, -1):
                sum_Rx = np.dot(R[i, i+1:], x[i+1:])
                x[i] = -sum_Rx / R[i, i] if R[i, i] != 0 else 0
        # converting into matrix 
            m = Matrix(n,1)

            for i in range(len(x)):
                m[i,0] = x[i]
            
            return m
    def dominantEigen(self):
        b = Matrix(self.n,1)
        b.toOne()
        b_old = Matrix(self.n,1)
        b_old.randomize()
        # print(type((self*b).norm(2)))
        for i in range(1000):
            b_old = b
            b = (self * b)/((self*b).norm(2))
            # b = (self * b)*1/np.linalg.norm((self*b).matrix,2)

        v = b
        # print(b.t()*b)
        deno = b.t()*b
        deno = deno[0,0]
        e =((b.t() * self) * b)/deno
        # print(type(e))
        e = e[0,0]
        return e,v
    def Power(self,A):
        b = Matrix(A.n,1)
        b.toOne()
        b_old = Matrix(A.n,1)
        b_old.randomize()
        # print(type((self*b).norm(2)))
        while b!=b_old:
            b_old = b
            b = (A * b)/((A*b).norm(2))
            # b = (self * b)*1/np.linalg.norm((self*b).matrix,2)

        v = b
        print(b.t()*b)
        deno = b.t()*b
        deno = deno[0,0]
        e =((b.t() * A) * b)/deno
        # print(type(e))
        return e,v
    def power_method(self, tol=1e-6, max_iter=1000):
        x = np.ones(self.n)  # Initial guess for the eigenvector
        x /= np.linalg.norm(x, ord=2)  # Normalize the initial guess

        for _ in range(max_iter):
            # Perform matrix-vector multiplication
            Ax = self.matrix.dot(x)

            # Compute the eigenvalue estimate
            eigenvalue = np.dot(Ax, x)

            # Normalize the result to get the next eigenvector approximation
            x_next = Ax / np.linalg.norm(Ax, ord=2)

            # Check for convergence
            if np.linalg.norm(x_next - x, ord=2) < tol:
                break

            x = x_next

        return eigenvalue, x
if __name__=="__main__":
    # m = Matrix(3,4)
    # m.toOne()
    # print(m)
    # m = Matrix(3, 4)
    # m[1, 1] = 2
    # m[2, 3] = 4
    # print(m)
    # --------------------------
    # m = Matrix(2, 3)
    # m.randomize()
    # print(m)
    # # m.t()
    # print(m.t())
    # --------------------
    # m1 = Matrix(2, 3)
    # m1.randomize()
    # print(m1)
    # m2 = Matrix(3, 2)
    # m2.randomize()
    # print(m2)
    # print(m1 + m2.t())

    # print(m2.t() - m1)

    # print(m1 * m2)
    # print(m1 * m2.t())

    # m = Matrix(2, 3)
    # m.randomize()
    # print(m)
    # m = 2.0 * m
    # print(m)
    # m = m * 3.0
    # print(m)

    # m = Matrix(2, 3)
    # m.randomize()
    # print(m)
    # print(m.norm(1))
    # print(m.norm(2))
    # print(m.norm(math.inf))

    m = Matrix(2, 3)

    for i in range(2):
        for j in range(3):
            m[i, j] = (i+1) + (j+1)
    print(m)
    print(m.solvezero())

    # m = Matrix(3, 3)
    # for i in range(3):
    #     for j in range(3):
    #         m[i, j] = (i+1) ** (j+1)
    # print(m)
    # e, v = m.dominantEigen()
    # print(e)
    # print(v)
    # m = Matrix(2,3)
    # m[0,0] = 0.69907995
    # m[0,1] = 0.74917486
    # m[0,2] = 0.91068809
    # m[1,0] = 0.94984428
    # m[1,1] = 0.65229157
    # m[1,2] = 0.40772897

    # print(m.norm(math.inf,math.inf))