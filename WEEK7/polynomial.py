import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.integrate as integrate

class Polynomial:
    def __init__(self,coeff):
        self.coeff = coeff
    def __call__(self,value):
        return self[value]
    def __str__(self):
        ans = "Coefficients of the polynomial are :\n"
        for c in self.coeff:
            ans+= str(c) + " "
        return ans
    
    def __add__(self,poly):
        if(type(poly)!=Polynomial):
            raise TypeError (" '+' not supported with types Polynomial and "+ str(type(poly)))
        diff = len(poly) - len(self)


        if (diff > 0):
            copyCoeff = np.array ([x for x in self.coeff])
            for i in range(diff):
                copyCoeff = np.append(copyCoeff,0)
            return Polynomial(poly.coeff + copyCoeff)
        else :
            copyCoeff = np.array ([x for x in poly.coeff])
            for i in range(-diff):
                copyCoeff = np.append(copyCoeff,0)
            return Polynomial(self.coeff + copyCoeff)
    
    def __sub__(self,poly):
        if(type(poly)!=Polynomial):
            raise TypeError (" '+' not supported with types Polynomial and "+ str(type(poly)))
        diff = len(poly) - len(self)


        if (diff > 0):
            copyCoeff = np.array ([x for x in self.coeff])
            for i in range(diff):
                copyCoeff = np.append(copyCoeff,0.0)
            return Polynomial(copyCoeff - poly.coeff)
        else :
            copyCoeff = np.array ([x for x in poly.coeff])
            for i in range(-diff):
                copyCoeff = np.append(copyCoeff,0.0)
            return Polynomial(self.coeff - copyCoeff)

    def __rmul__(self,r1):
        if type(r1)==int or type(r1)==float:
            result = [r1 * x for x in self.coeff]
        return Polynomial(result)
    
    def __mul__(self,r1):
        if isinstance(r1,Polynomial):
            result = [0] * (len(r1.coeff) + len(self.coeff)-1)
        for i in range(len(self.coeff)):
            for j in range(len(r1.coeff)):
                result[i+j] += self.coeff[i] * r1.coeff[j]
        return Polynomial(result)
    def __getitem__(self,value):
        return sum([self.coeff[p]* (value**p) for p in range(len(self.coeff))])
    
    def __len__(self):
        return len(self.coeff)
    
    def show(self,a,b):

        def f(x):
            c = 1
            f_x = 0
            for i in self.coeff:
                f_x += c*i
                c*=x
            return f_x
        x_values = np.linspace(a,b,100)
        y = f(x_values)
        function_expression = ' + '.join([f'{self.coeff[i]}x^{i}' for i in range(len(self.coeff))])
        plt.plot(x_values,y)

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Plot of $y = {function_expression}$')
        # plt.show()

    def fitViaMatrixMethod(self, points,showPlot = True):
        b = []
        A = []
        length = len(points)
        for x,y in points:
            b.append(y)
            A.append([x**i for i in range(length)])
        x = np.linalg.solve(A,b)
        self.coeff = np.array([float(i) for i in x])
        if showPlot:
        # Plotting the points and the curve
            x_values = np.linspace(min(point[0] for point in points), max(point[0] for point in points), 100)
            y_values = sum(self.coeff[i] * x_values**i for i in range(length))

            plt.scatter([point[0] for point in points], [point[1] for point in points], color='red', label='Given Points')
            plt.plot(x_values, y_values, label='Fitted Curve')

            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Fitted Curve')
            plt.legend()

            plt.show()

    def fitViaLagrangePoly(self,points):
        n = len(points)
        X = [x for x,_ in points]
        Y = [y for _,y in points]

        def lagrange(j):
            pi = Polynomial([1])
            for i in range(n):
                if i!=j :
                    pi*= Polynomial([-X[i]/(X[j]-X[i]),1/(X[j]-X[i])])
            return pi

        P = Polynomial([0])

        for i in range(n):
            P += Y[i]*lagrange(i)
        print(P)
        self.coeff = np.array([i for i in P.coeff])
        print(self.coeff)
        # Plotting the points and the curve
        x_values = np.linspace(min(X), max(X), 100)
        y_values = [self[i] for i in x_values]

        plt.scatter([point[0] for point in points], [point[1] for point in points], color='red', label='Given Points')
        plt.plot(x_values, y_values, label='Fitted Curve')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Fitted Curve')
        plt.legend()

        plt.show()

    def derivative(self):
        coeff = self.coeff
        newCoeff = []
        for i in range(1,len(coeff)):
            newCoeff.append( i*coeff[i])
        return Polynomial(newCoeff)
