def root(n,a,e):
    f = lambda x : x**n - a
    B = a
    A = 0
    while abs(B-A) > e :
        c = (A+B)/2
        if (f(c)*f(A) > 0):
            A = c
        else:
            B = c
    return (A+B)/2

if __name__ == "__main__":
    nthRoot = root (3,2,0.0001)
    print(nthRoot)