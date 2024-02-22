from Qn1 import f_prime, f_prime_bfd,f_prime_cfd,f_prime_ffd
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0,1,100)

er_plus = [abs(f_prime(x)-f_prime_ffd(x)) for x in X]
er_minus = [abs(f_prime(x)-f_prime_bfd(x)) for x in X]
er_c = [abs(f_prime(x)-f_prime_cfd(x)) for x in X]

plt.plot(X,er_plus,label = 'FFD')
plt.plot(X,er_minus,label = 'BFD')
plt.plot(X,er_c,label = 'CFD')
plt.title('errors')
plt.xlabel('X')
plt.ylabel('F prime')
plt.legend()

plt.grid()
plt.show()
