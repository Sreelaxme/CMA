
from math import e
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

g = lambda x : e**(-x)



def findUxt(hx,ht,Tmax,xc,yc):
    
    a = 0
    b = 1

    N = int((b-a)/hx)

    ArrX = np.linspace(a,b,N+1)

    u = [[[0 for y in ArrX] for x in ArrX]]
    

    ti = 0 
    te = Tmax
    Nt = int ((te-ti)/ht)

    ArrT = np.linspace(ti,te,Nt+1)
    
    f = lambda x,y : e**(-(((x-xc)**2 + (y-yc)**2)**(0.5)))

    F = lambda i,j,t :  (u[t-1][i+1][j]+ u[t-1][i-1][j] - 2*u[t-1][i][j])/(hx**2) + \
                        (u[t-1][i][j+1]+ u[t-1][i][j-1] - 2*u[t-1][i][j])/(hx**2) + \
                        f(ArrX[i],ArrX[j])
    

    for t in range(1,Nt+1):
        temp = [[0 for y in ArrX] for x in ArrX]
        for i in range(N+1):
            for j in range(N+1):
                if(ArrX[i] == 0 or ArrX[i] == 1 or ArrX[j] == 0 or ArrX[j] == 1):
                    temp[i][j] = 0 
                else:
                    temp[i][j] = u[t-1][i][j] + ht*(F(i,j,t))
        u.append(temp)

    return u


def visualize (xc=0.5,yc=0.5):
    l = 1/4
    hx = 0.1 * l  #0.05
    ht = 0.001 * l**2  #0.00025

    a = 0
    b = 1
    # hx = 0.01
    N = int((b-a)/hx)

    ArrX = np.linspace(a,b,N+1)

    Tmax = 0.1

    ti = 0 
    te = Tmax
    Nt = int ((te-ti)/ht)
    

    u = findUxt(hx,ht,Tmax,xc,yc)
    # print(np.array(u))
    # #-------animate--------
    fps = 25
    slowF = 20
    # fig, ax = plt.subplots()
    fig = plt.figure()

    # im = ax.imshow(u[0], cmap='hot', interpolation='nearest')  

    factor = int(1/(fps*ht*slowF))
    im = plt.imshow(u[0*factor], cmap='hot')
    cbar = plt.colorbar(im)
    cbar.ax.tick_params(labelsize=8)

    def animate(i):
        im = plt.imshow(u[i*factor], cmap='hot')
        return im,

    ani = animation.FuncAnimation(fig, animate, frames=int(fps*(te-ti)*slowF), interval=1000/fps)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("The variation of temperature over a period of "+str(Tmax)+"s.("+str(slowF)+" x slower)")
    plt.show()

if __name__ == "__main__":
    visualize(0.1,0.5)