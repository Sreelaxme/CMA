import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
from scipy.integrate import solve_ivp
import numpy as np
from scipy.signal import find_peaks

def van_der_pol(mu,x0,t0,T, v0,n):
    def fdash(t,y):
        x,v = y
        return [v,mu*(1-x**2)*v-x]

    t_eval = np.linspace(t0,T,n)
    # solve the ODEs
    sol = solve_ivp(fdash,t_span = [t0,T], y0 = [x0,v0],t_eval = t_eval)
    plt.plot(t_eval,sol.y[0])
    pks,_ = find_peaks(sol.y[0])
    time_period = np.mean(np.diff(t_eval[pks]))
    print(f"time period for mu = {mu} is {time_period:4f}")
    plt.title(f"Van der pol equation for {mu}")
    plt.grid()
    plt.show()

van_der_pol(x0=0, v0=5, mu=0.05, t0=0, T=100, n=1000)
    