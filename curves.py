import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
m = 1
x = np.linspace(1,10,10)
y = m*x + 5

w1 = np.linspace(-10,10,200)
w0 = np.linspace(-10,10,200)
W0, W1 = np.meshgrid (w0, w1)
l = 0
it = len(x)
for i in range(it):
	l += (W1*x[i] + W0 - y[i])**2
plt.gca().set_aspect('equal',adjustable = 'box') #to make the graph square
plt.draw()
plt.xlabel('w0')
plt.ylabel('w1')
plt.title('w1 vs w0 (Level graph)')
plt.contour(W0,W1,l,levels = [i for i in np.arange(-200,200,60)],colors = "black")
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(W0, W1, l, cmap='viridis', rstride=1, cstride=1, edgecolor='none')
plt.show()
