#dependencies: numpy, matplotlib
import numpy
import matplotlib.pyplot as plot
import matplotlib.animation as animate

#define plot area
X=numpy.linspace(0,2*numpy.pi,100)
Y=numpy.sin(X)

#show plot area
bg_img=plot.imread("image.jpg")
fig, ax=plot.subplots(1,1)
ax.imshow(bg_img, extent=[0,2*numpy.pi,-1.1,1.1])
ax.set_xlim([0,2*numpy.pi])
ax.set_ylim([-1.1,1.1])

#show plot object
sinegraph,=ax.plot([],[])
dot,=ax.plot([],[],'o',color='red')

def sinewave(i):
    sinegraph.set_data(X[:i],Y[:i])
    dot.set_data(X[i],Y[i])

animation = animate.FuncAnimation(fig,sinewave,frames=len(X),interval=50)
plot.show()