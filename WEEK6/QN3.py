import numpy as np
pi = np.pi
import matplotlib.animation as animation
import matplotlib.pyplot as plt
def pendulumSim(initTheta = pi/3,initOmega = 0):
    h = 0.001
    s = 10
    fps = 25
    ms = int(1000/fps)
    factor = int(1/(fps*h))
    
    L = 2
    g = 10
    X = np.arange(0,10+h,h)
    t = []
    thetaDot = [initOmega]
    theta = [initTheta]
    ti=0
    while ti <= s:
        t.append(ti)
        ti += h
    for i in X:
        if i==0: continue
        newthetaDot = thetaDot[-1] - h*(g*np.sin(theta[-1]))/L
        thetaDot.append(newthetaDot)
        newTheta = theta[-1]+thetaDot[-2]*h
        theta.append(newTheta)

    # return theta
        

# if __name__=="__main__":
    fig = plt.figure()
    axis = plt.axes(xlim = (-4,4),ylim=(-4,4))
    
    pendulum, = axis.plot([],[])
    dot = axis.scatter([], [],s = 100,color = "r", label = "bob")
    # print(type(pendulum))
    x_frm_ang = lambda t: L*np.sin(theta[factor*t])
    y_frm_ang = lambda t: -L*np.cos(theta[factor*t])

    plt.grid()
    def update(i):
            fps = 25
            h = 0.001
            factor = int(1/(fps*h))

            theta = pendulumSim()
            L = 2
            # Calculate the position of the pendulum bob
            x = [0,x_frm_ang(i)]
            y = [0,y_frm_ang(i)]

            # Update the position of the pendulum bob
            pendulum.set_data([0, x], [0, y])
            dot.set_offsets([x,y])
            return pendulum,dot

    # call the animation function
    anim = animation.FuncAnimation(fig, update,
                                frames = s*fps,)

    # Show animation
    plt.show()

# def init():
#     # [line.set_data([],[]) for line in lines]
#     pendulum.set_data([0,2],[0,0])
#     return pendulum

if __name__=="__main__":
    pendulumSim()