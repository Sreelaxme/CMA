import matplotlib.pyplot as plt 
import numpy as np 
import math
from matplotlib.animation import FuncAnimation 
e = math.e

g = lambda x : e**(-x)

def findUxt(hx,ht,Tmax):
    a = 0
    b = 1
    N = int((b-a)/hx)

    ArrX = np.linspace(a,b,N+1)
    t = a 
    u = [[g(x)] for x in ArrX]
    ti = 0 
    te = Tmax
    Nt = int((te-ti)/ht)

    ArrT = np.linspace(ti,te,Nt+ 1)
    f = lambda i,j :  (u[i-1][j-1] + u[i+1][j-1]-2*u[i][j-1])/(hx**2)

    for j in range(1,Nt+1):
        for i in range(N+1):
            if ArrX[i]==0 or ArrX[i] == 1:
                u[i].append(0)
            else:
                u[i].append(u[i][j-1]+ht * f(i,j))

    return u

def visualize():
    hx = 0.05
    ht = 0.00025
    a = 0
    b = 1 
    N = int((b-a)/hx)

    ArrX = np.linspace(a,b,N+1)

    Tmax = 1

    ti = 0 
    te = Tmax
    Nt = int ((te-ti)/ht)
    

    u = findUxt(hx,ht,Tmax)
    # ------------------------------------------------
    fps = 25
    slowF = 5 
    fig,ax = plt.subplots()
    line, = ax.plot([],[],color='r',label = "u")
    ax.set_ylim([0,1])
    ax.set_xlim([0,1])

    factor = int(1/(fps*ht*slowF))

    def animate(i):
        temp = [u[k][factor*i] for k in range(len(u))]
        line.set_data(ArrX,temp)
        return line,

    ani = FuncAnimation(fig,animate,blit = True)
    plt.show()

if __name__ == "__main__":
    visualize()