from pylab import *

n = 8
X,Y = np.mgrid[0:n,0:n]
quiver(X,Y), show()