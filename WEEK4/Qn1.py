import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.sin(x)

def f_prime(x):
    return np.cos(x **2) * 2 * x

def f_prime_ffd(x):
  return (f((x+ 0.01)**2) - f(x**2))/0.01

def f_prime_bfd(x):
   return (-f((x- 0.01)**2) + f(x**2))/0.01

def f_prime_cfd(x):
   return (-f((x- 0.01)**2) + f((x+0.01)**2))/0.02

X = np.linspace(0,1,100)

y_f_prime = f_prime(X)
y_f_prime_ffd_ = f_prime_ffd(X)

plt.plot(X,y_f_prime,label = 'Actaul')
plt.plot(X,y_f_prime_ffd_,label = 'FFD')
plt.xlabel('X')
plt.ylabel('F prime')
plt.legend()
plt.grid()
plt.show()
