import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from math import sin,pi,cos

g = 9.8
L = 1
theta_dot_dot = lambda x : -g/L * sin(x)

def pendulum(s=10,initTheta = pi/3,initOmega = 0):
    theta = [initTheta]
    theta_dot = [initOmega]
    t = []
    h= 0.001
    fps = 25
    ms = int(1000/fps)
    factor = int(1/(fps*h))
    ti = 0
    while ti<=s:
        t.append(ti)
        ti+=h

    for ti in t[1:]:
        newTheta = theta[-1]+ h * theta_dot[-1]
        theta.append(newTheta)

        newTheta_dot = theta_dot[-1] + h * theta_dot_dot(theta[-2])
        theta_dot.append(newTheta_dot)

    # -------------------------------------------
    fig , ax = plt.subplots()
    line, = ax.plot([],[],color = 'black')
    # line1, = ax.plot([],[],color='r')
    dot = ax.scatter([],[],s=100,color = 'r')
    ax.set_xlim([-1.5*L,1.5*L])
    ax.set_ylim([-1.5*L,1.5*L])
    x_frm_ang = lambda t : L * sin(theta[factor*t])
    y_frm_ang = lambda t : -L * cos(theta[factor*t])

    def animate(i):
        x = [0,x_frm_ang(i)]
        y = [0,y_frm_ang(i)]

        line.set_data(x,y)
        dot.set_offsets([(x[1],y[1])])
        return line,dot
    ani = animation.FuncAnimation(fig,animate)
    plt.scatter([0],[0],label = 'pivot',color = 'black')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    pendulum()
