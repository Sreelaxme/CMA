
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def dis (p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    p1 = np.array([x1,y1])
    p2 = np.array([x2,y2])
    # return (((x1-x2)**2)+((y1-y2)**2))**0.5
    return np.linalg.norm(p2-p1)


def ax (p1,p2):
    x1,y1 = p1
    x2,y2 = p2

    return (x2-x1)/((dis(p1,p2))**3)

def ay (p1,p2):
    x1,y1 = p1
    x2,y2 = p2

    return (y2-y1)/((dis(p1,p2))**3)

def odesystem(t, y):
    x1,vx1,y1,vy1,x2,vx2,y2,vy2, x3,vx3,y3,vy3 = y
    p1 = (x1,y1)
    p2 = (x2,y2)
    p3 = (x3,y3)

    dydt = [vx1, ax(p1,p2) + ax(p1,p3),vy1, ay(p1,p2) + ay(p1,p3), 
            vx2, ax(p2,p1) + ax(p2,p3),vy2, ay(p2,p1) + ay(p2,p3),
            vx3, ax(p3,p1) + ax(p3,p2),vy3, ay(p3,p1) + ay(p3,p2)]
    return dydt

def visualize (P1,P2,P3,t_end= 200, anim = True):
    
    t_span = (0, t_end)
    y0 = [P1[0],0,P1[1],0, P2[0],0,P2[1],0, P3[0],0,P3[1],0]
    sol = solve_ivp(odesystem, t_span, y0, method='RK45', t_eval=np.linspace(0, t_end, t_end*10+1))

    p1x = sol.y[0]
    p1y = sol.y[2]

    p2x = sol.y[4]
    p2y = sol.y[6]

    p3x = sol.y[8]
    p3y = sol.y[10]

    if(not anim):
        plt.scatter([P1[0]],[P1[1]],label="p1-start", color = "b")
        plt.scatter([P2[0]],[P2[1]],label="p2-start", color = "y")
        plt.scatter([P3[0]],[P3[1]],label="p3-start", color = "r")
        plt.plot(p1x, p1y, label='1-trajectory',color = "b")
        plt.plot(p2x, p2y, label='2-trajectory',color = "y")    
        plt.plot(p3x, p3y, label='3-trajectory',color = "r")

    else:
    #--------animate----------
        ms = 20
        fig, ax = plt.subplots()

        line1, = ax.plot([], [],color = "b")
        line2, = ax.plot([], [],color = "y")
        line3, = ax.plot([], [],color = "r")

        dot1 = ax.scatter([], [],s = 50,color = "b",label = "p1")
        dot2 = ax.scatter([], [],s = 50,color = "y",label = "p2")
        dot3 = ax.scatter([], [],s = 50,color = "r",label = "p3")
        
        minx = min(min(p1x),min(p2x),min(p3x))
        maxx = max(max(p1x),max(p2x),max(p3x))
        xtraX = (maxx-minx)/8
        miny = min(min(p1y),min(p2y),min(p3y))
        maxy = max(max(p1y),max(p2y),max(p3y))
        xtraY = (maxy-miny)/8


        ax.set_xlim([minx - xtraX , maxx + xtraX ])
        ax.set_ylim([miny - xtraY , maxy + xtraY ])

        def animate(i):
            line1.set_data(p1x[:i+1],p1y[:i+1])
            line2.set_data(p2x[:i+1],p2y[:i+1])
            line3.set_data(p3x[:i+1],p3y[:i+1])

            dot1.set_offsets([ (p1x[i],p1y[i]) ])
            dot2.set_offsets([ (p2x[i],p2y[i]) ])
            dot3.set_offsets([ (p3x[i],p3y[i]) ])

            return line1,line2,line3,dot1,dot2,dot3

        ani = animation.FuncAnimation(fig, animate, frames=len(p1x), interval=ms, blit=True)
        writer = animation.PillowWriter(fps=30)
        ani.save('my_animation.gif', writer=writer)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title("Trajectory of 3 mutually attracting body.")
    plt.grid()
    plt.show()



if __name__ == "__main__":

    #----trivial-starting-points-----
    # p1 = (-10,0)
    # p2 = (10/2,(3**0.5)*10/2)
    # p3 = (10/2,-(3**0.5)*10/2)


    p1 = (-10,0)
    p2 = (0,10)
    p3 = (20,0)

    visualize(p1,p2,p3,200,True)       # make the 5th parameter True to see the animation, False to see the trajectory only.