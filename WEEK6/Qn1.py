import matplotlib.pyplot as plt
import numpy as np

f = lambda x : -2*x
def forward_euler(x0,t0,T,h):

    xn = [x0]
    points = np.arange(0,10,h)
    for i in range(len(points)-1):
        xi = xn[-1] + h * f(xn[-1])
        xn.append(xi)

    poly = np.polyfit(points,xn,len(points)-1)
    # X = np.linspace(0,10,110)
    y = np.polyval(poly,points)
    plt.plot(points,y,label=f'h = {h}')

def plots(H,x0,t0,T):
    for h in H:
        forward_euler(x0,t0,T,h)
    actual = lambda x : 5 * np.e**(-2*x)
    X = np.linspace(0,10,100)
    Y = actual(X)
    plt.plot(X,Y,label = 'actual')
    plt.legend()
    plt.show()

if __name__ =="__main__":
    plots([0.1,0.5,1,2,3],5,0,10)

