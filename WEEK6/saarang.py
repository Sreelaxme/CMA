
import matplotlib.pyplot as plt
from math import sin,pi,cos
import matplotlib.animation as animation


g = 9.8
L = 1

thetta_dot_dot = lambda x: -g/L * sin(x)


def simulate_pendulum (s = 10,initTetta = pi/3,initOmega = 0):
    thetta = [initTetta]
    thetta_dot = [initOmega]
    t = []
    h = 0.001
    fps = 25
    ms = int(1000/fps) # time interval between two frames in ms
    factor = int(1/(fps*h))
    ti = 0
    
    while ti <= s:
        t.append(ti)
        ti += h

    for ti in t[1:]:
        newThetta = thetta[-1] + h*thetta_dot[-1]
        thetta.append(newThetta)

        newThetta_dot = thetta_dot[-1] + h*thetta_dot_dot(thetta[-2])
        thetta_dot.append(newThetta_dot)

    # print(t[-1])
    #----------animation-----------
    fig, ax = plt.subplots()

    line, = ax.plot([], [],color = "black", label = "cord")
    line1, = ax.plot([], [],color = "r", label = "shadow",lw = 2.5)

    dot = ax.scatter([], [],s = 100,color = "r", label = "bob")
    
    ax.set_aspect('equal') 
    ax.set_xlim([-1.5*L, 1.5*L])
    ax.set_ylim([-1.5*L, 1.5*L])

    


    def animate(i):
        x = [0,x_frm_ang(i)]
        y = [0,y_frm_ang(i)]

        gx = [x_frm_ang(i) for i in range(max(0,i-10),i+1)]
        gy = [y_frm_ang(i) for i in range(max(0,i-10),i+1)]

        line.set_data(x,y)
        line1.set_data(gx,gy) 
        dot.set_offsets([ (x[1],y[1]) ])
        return line,dot,line1

    ani = animation.FuncAnimation(fig, animate, frames=s*fps, interval=ms, blit=True)

    #------------------------------
    
    
    plt.scatter([0],[0], label = "pivot", color = "black")
    # plt.axis("equal")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    simulate_pendulum( )