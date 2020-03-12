import numpy
import matplotlib.pyplot as plotter
import scipy.interpolate as interpolate

#input the coordinates here
x_axis = numpy.array([1,4,7,11])
y_axis = numpy.array([3,5,6,10])

plotter.figure()
startPlot = plotter.plot(x_axis, y_axis, "ro")

param1 = numpy.linspace(0, 1, len(x_axis))
x_Interpolate = interpolate.lagrange(param1, x_axis)
y_Interpolate = interpolate.lagrange(param1, y_axis)
numSlices = 1000

param2 = numpy.linspace(param1[0], param1[-1], numSlices)
x_coordinate = x_Interpolate(param2)
y_coordinate = y_Interpolate(param2)
plotter.plot(x_coordinate, y_coordinate, "b-", label="Polynomial")

plotter.show()