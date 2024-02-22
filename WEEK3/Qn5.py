

from scipy import interpolate
import matplotlib.pyplot as plt
import random as rn
import numpy as np
from matplotlib.animation import FuncAnimation

def objective_function(x):
    return np.tan(x)*np.sin(30*x)*np.exp(x)

def init():
    [line.set_data([],[]) for line in lines]
    return lines

def animate(i):
    x = np.linspace(0,1,100)
    y_true  = [objective_function(i) for i in x]

    i = i+2
    x_sampled = sorted(rn.sample(list(x),i))
    y_sampled = [objective_function(a) for a in x_sampled]
    cs = interpolate.CubicSpline(x_sampled, y_sampled)
    akima = interpolate.Akima1DInterpolator(x_sampled, y_sampled)
    bary = interpolate.BarycentricInterpolator(x_sampled, y_sampled)

    # Calculate interpolated values
    y_cs = cs(x)
    y_akima = akima(x)
    y_bary = bary(x)

    # Draw each graph
    line_true.set_data(x, y_true)
    line_cs.set_data(x, y_cs)
    line_akima.set_data(x, y_akima)
    line_bary.set_data(x, y_bary)

    # Update title
    plt.title("Interpolations of tan(x) sin(30x) $e^x$ for "+ str(i) + " samples")

    return lines
if __name__=="__main__":
    fig = plt.figure()
    axis = plt.axes(xlim = (-0.02,1.02),ylim=(-4,4))

    line_true, = axis.plot([],[])
    line_cs, = axis.plot([],[])
    line_akima, = axis.plot([],[])
    line_bary, = axis.plot([],[])

    lines = [line_true,line_cs,line_akima,line_bary]
    
    plt.grid()
    line_true.set_label("True")
    line_cs.set_label("Cubic Spline")
    line_akima.set_label("Akima")
    line_bary.set_label("Barycentre")
    plt.legend(loc="upper left")
    plt.xlabel("x")
    plt.ylabel("f(x)")

    # call the animation function
    anim = FuncAnimation(fig, animate, init_func = init,
                                frames = 40)
    
    # Show animation
    plt.show()

