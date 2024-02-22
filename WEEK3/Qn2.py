from Qn1 import RowVectorFloat
import math
import random
import numpy as np

class SquareMatrixFloat:
    def __init__(self,n):
        self.n = n
        self.rows = [RowVectorFloat([0]*n) for _ in range(n)]

    def __str__(self):
        ans = "The matrix is: \n"
        for row in self.rows:
            ans+=str(row)+"\n"
        return ans
    def sampleSymmetric(self):
        for i in range(self.n):
            self.rows[i][i] = round(random.uniform(0, self.n), 2)
        for i in range(self.n):
            for j in range(i+1,self.n):
                a = round(random.uniform(0,1),2)
                self.rows[i][j] = a
                self.rows[j][i] = a

    def toRowEchelonForm(self):
        """
        Convert matrix to row echelon form
        """
        for i in range(self.n):
            # Convert diagonal elements to 1
            self.rows[i] = self.rows[i] / self.rows[i][i]

            # Use a linear combination of the current row and the rows below to set low triangular elements to 0
            for j in range(i + 1, self.n):
                factor = self.rows[j][i] / self.rows[i][i]
                self.rows[j] = self.rows[j] - factor * self.rows[i]
                if self.rows[j]== -0.0:
                    self.rows[j] = 0.0

    def isDRDominant(self):
        diagonal=0
        nonDiagonal = 0
        for i in range(self.n):
            for j in range(self.n):
                if j == i :
                    diagonal+=self.rows[i][j]
                else:
                    nonDiagonal+=self.rows[i][j]
            return diagonal>nonDiagonal
        
    def jSolve(self,b,m):
        if not self.isDRDominant():
            raise Exception("Not solving because convergence is not guaranteed")
        x = [0]*self.n
        errors = []
        for iterations in range(m):
            x_new = x.copy()
            for i in range(self.n):
                x_new[i] = (1/self.rows[i][i])*(b[i]-sum(self.rows[i][j]*x[j] for j in range(self.n) if j!=i))
            x = x_new
            residual= np.array([-float(b[i]) for i in range(self.n)])
            for i in range(self.n):
                for j in range(self.n):
                    residual[i]+=self.rows[i][j]*x[j]
            residual_norm = np.linalg.norm(residual, 2)

        # Append the 2-norm of the residual to the errors list
            errors.append(residual_norm)

        return errors,x
    
    def gsSolve(self,b,m):
        if not self.isDRDominant():
            raise Exception("Not solving because convergence is not guaranteed")
        x = [0]*self.n
        errors = []
        for iterations in range(m):
        
            for i in range(self.n):
                x[i] = (1/self.rows[i][i])*(b[i]-sum(self.rows[i][j]*x[j] for j in range(self.n) if i!=j))
        
            residual= np.array([-float(b[i]) for i in range(self.n)])
            for i in range(self.n):
                for j in range(self.n):
                    residual[i]+=self.rows[i][j]*x[j]
            residual_norm = np.linalg.norm(residual, 2)

        # Append the 2-norm of the residual to the errors list
            errors.append(residual_norm)
        return (errors,x)
    

if __name__ == "__main__":
    s = SquareMatrixFloat(4)
    s.sampleSymmetric()
    print(s.isDRDominant())
    s.toRowEchelonForm()
    print(s)