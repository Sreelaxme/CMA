from polynomial import Polynomial
import random
import numpy as np

def aberth_method(P:Polynomial, e , Z):
    """Z is the initial guesses
    """
    n = min(len(P.coeff)-1, len(Z))

    if n == 0 :
        return None
    
    Z0 = [z+10*e for z in Z]

    while any([abs(Z[i] - Z0[i]) > e for i in range(n)]):
        """
        for all k
        z_k(t+1) = z_k(t) - 1/(P'(z_k(t))/P(z_k(t)) - sum(z_k - z_j for all j, k != j))

        halts when change in each root estimate is less than ɛ.
        """
        memo = [sum([1/(Z[k]-Z[j]) if k!=j else 0 for j in range(n)]) for k in range(n)]
        Z0 = Z.copy()
        for i in range(n):
            t = P(Z[i])/P.derivative()(Z[i])
            Z[i] -= t / (1-t*memo[i])

        return Z

Polynomial.printRoots = lambda self,Z0 : aberth_method(self,10e-3,Z0)

if __name__ == '__main__':

    # Test case 1: p1 has two real roots
    p1 = Polynomial([-1, 0, 1])
    print("x² - 1")
    print(p1.printRoots([-2, 0.5]))
    print()
