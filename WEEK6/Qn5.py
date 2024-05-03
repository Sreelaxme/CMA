from scipy.integrate import solve_ivp
from scipy.signal import find_peaks
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.lines import Line2D

def three_body_problem(r0,v0,t0,T,n):
    def get_norm(r1,r2):
        return np.linalg.norm(r2-r1)
    def double_derivative(r1,r2,r3):
        norm1 = get_norm(r2,r1)**3
        norm2 = get_norm(r3,r1)**3
        derivative = ((r2-r1)/norm1) + ((r3-r1)/norm2)
        return list(derivative)

    def three_derivatives(t,y):
        r1,r2,r3,v1,v2,v3 = np.reshape(y, (6, 2))
        dd1 = double_derivative(r1,r2,r3)
        dd2 = double_derivative(r2,r3,r1)
        dd3 = double_derivative(r3,r1,r2)
        dd = np.concatenate((v1,v2,v3,dd1,dd2,dd3))
        return dd

    t = np.linspace(t0,T,n)
    sol = solve_ivp(three_derivatives,[t0,T],y0=[*r0,*v0],t_eval = t,method = 'RK45')
    print(len(sol.y))
    r1x,r1y,r2x,r2y,r3x,r3y,_,_,_,_,_,_ = sol.y

    fig,ax = plt.subplots()
    bob_radius = 0.1
    line1, = ax.plot([], [],color = 'b')
    line2, = ax.plot([], [],color = "y")
    line3, = ax.plot([], [],color = "r")
    body1 = ax.add_patch(plt.Circle((r1x[0],r1y[0]),bob_radius,color='r'))
    body2 = ax.add_patch(plt.Circle((r2x[0],r2y[0]),bob_radius,color='b'))
    body3 = ax.add_patch(plt.Circle((r3x[0],r3y[0]),bob_radius,color='g'))

    bodies = [line1,line2,line3,body1,body2,body3]

    def init():
        ax.set_title("Three body")
        minx = min(min(r1x),min(r2x),min(r3x))
        maxx = max(max(r1x),max(r2x),max(r3x))
        xtraX = (maxx-minx)/8
        miny = min(min(r1y),min(r2y),min(r3y))
        maxy = max(max(r1y),max(r2y),max(r3y))
        xtraY = (maxy-miny)/8
        ax.set_xlim([minx - xtraX , maxx + xtraX ])
        ax.set_ylim([miny - xtraY , maxy + xtraY ])
        # return bodies 
    
    def animate(i):
        line1.set_data(r1x[:i+1],r1y[:i+1])
        line2.set_data(r2x[:i+1],r2y[:i+1])
        line3.set_data(r3x[:i+1],r3y[:i+1])
        body1.set_center((r1x[i],r1y[i]))
        body2.set_center((r2x[i],r2y[i]))
        body3.set_center((r3x[i],r3y[i]))
        bodies = [line1,line2,line3,body1,body2,body3]
        return bodies 
    
    anim = animation.FuncAnimation(fig,animate,frames = len(r1x),init_func=init, interval = 1,blit = True)

    # Making custom legend
    line1a = Line2D([], [], color="red", marker='o', markersize=7, markerfacecolor="red")
    line2a = Line2D([], [], color="blue", marker='o', markersize=7, markerfacecolor="blue")
    line3a = Line2D([], [], color="green", marker='o', markersize=7, markerfacecolor="green")
    plt.legend((line1a, line2a, line3a), ('Body 1', 'Body 2', 'Body 3'), numpoints=1, loc=1)
    plt.show()


if __name__ == "__main__":
    # three_body_problem([*[0, 0], *[3, math.sqrt(3)], *[3, -math.sqrt(3)]],[*[0,0],*[0,0],*[0,0]],0,800,2000)
        three_body_problem([*[-10, 0], *[0,10], *[20,0]],[*[0,0],*[0,0],*[0,0]],0,800,2000)