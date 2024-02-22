from polynomial import Polynomial

def derivative(P: Polynomial):
    coeff = P.coeff
    newCoeff = []
    for i in range(1,len(coeff)):
      newCoeff.append( i*coeff[i])

    return Polynomial(newCoeff)

Polynomial.derivative = derivative

def area(P:Polynomial,a,b):
    coeff = P.coeff
    newCoeff = [0]
    for i in range(len(coeff)):
      newCoeff.append(P.coeff[i]/(i+1))


    areaA = sum(newCoeff[i]*(a**i) for i in range(len(newCoeff)))
    areaB = sum(newCoeff[i]*(b**i) for i in range(len(newCoeff)))

    # print(areaA)
    # print(areaB)
    return areaB - areaA

Polynomial.area = area

p = Polynomial([1, 2, 3])
pd = p.derivative()
print(pd)

p = Polynomial([1, 2, 3])
print(p.area(1,2))
