import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
pi = np.pi
def pendulumSim(initTheta = pi/2,initOmega = 0,s = 10):
    t = []
    h = 0.01
    L = 2
    g = 10
    X = np.arange(0,10+h,h)
    thetaDot = [initOmega]
    theta = [initTheta]
    for i in X:
        if i==0: continue
        newthetaDot = thetaDot[-1] - h*(g*np.sin(theta[-1]))/L
        thetaDot.append(newthetaDot)
        newTheta = theta[-1]+thetaDot[-2]*h
        theta.append(newTheta)

    return theta

def init():
    # [line.set_data([],[]) for line in lines]

    pendulum.set_data([0,2],[0,0])
    return pendulum
def update(frame):
    theta = pendulumSim()
    L = 2
    # Calculate the position of the pendulum bob
    x = L * np.sin(theta[frame])
    y = -L * np.cos(theta[frame])

    # Update the position of the pendulum bob
    pendulum.set_data([0, x], [0, y])
    return pendulum
if __name__=="__main__":
    fig = plt.figure()
    axis = plt.axes(xlim = (-4,4),ylim=(-4,4))

    pendulum, = axis.plot([],[])


    plt.grid()


    # call the animation function
    anim = animation.FuncAnimation(fig, update, init_func = init,
                                frames = 100)

    # Show animation
    plt.show()
