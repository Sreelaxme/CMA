import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from IPython.display import HTML

fig,ax = plt.subplots()
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
line, = ax.plot([],[],color = 'green')
dot = ax.scatter([],[],color = 'red')
plt.scatter([0],[0],color = 'black')
theta0 = np.pi/3
omega0 = 0
theta = [theta0]
omega = [omega0]

t = np.arange(0,10.1,.1)
for i in range(len(t)):
  theta1 = theta[-1]
  omega1 = omega[-1]
  theta.append(theta1+0.1*omega1)
  omega.append(omega1-9.8*np.sin(theta1)*0.1)
  

def animate(frames):
  theta1 = theta[i] 
  x = [0,np.sin(theta1)]
  y = [0,np.cos(theta1)]
  line.set_data(x,y)
  dot.set_offsets([(np.sin(theta1),np.cos(theta1))])
  return line,dot


ani = FuncAnimation(fig,animate, frames = 100)
# ani.to_html5_video()
plt.show()