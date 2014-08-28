import numpy
import matplotlib.pyplot as plt

# use the sign convention and formulae provided by Lanchester (1909)

# calculate the radius of curvature of the flight path at any point
def radius_of_curvature(y, yt, C):
#	return 2./(C*(1./y)**1.5 - 2./3./yt)
        return -1*yt / (1./3 - C/2.*(yt/y)**1.5)

# given the coordinates of a point, the center around which it much revolve,
# and the angle of rotation, calculate the new position of the point
def rotate(x, y, xCenter, yCenter, angle):
	dx = x - xCenter
	dy = y - yCenter
	xNew = dx*numpy.cos(angle) - dy*numpy.sin(angle)
	yNew = dx*numpy.sin(angle) + dy*numpy.cos(angle)
	return xCenter + xNew, yCenter + yNew

# plot the flight path. The inputs are the trim height and the initial position 
# and orientation of the aircraft
def plot_flight_path(yt, y0, theta0):	
	# arrays to store the coordinates of the flight path
	N = 1000
	y = numpy.zeros(N)
	x = numpy.zeros(N)

	# set initial conditions
	y[0] = y0
	x[0] = 0.
	theta = theta0

	# calculate the constant C
	#C = numpy.sqrt(y[0])*(numpy.cos(theta) - y[0]/yt/3.)
        C = (numpy.cos(theta) - 1./3*y[0]/yt)*(y[0]/yt)**.5

	# incremental distance along the flight path
        ds = 1 
        
        #obtain the curve coordinates
	for i in xrange(1,N):
		normal = numpy.array([numpy.cos(theta+numpy.pi/2.), numpy.sin(theta+numpy.pi/2.)])
		R = radius_of_curvature(y[i-1], yt, C)
		center = numpy.array([x[i-1]+normal[0]*R, y[i-1]+normal[1]*R])
		dtheta = ds/R
		x[i], y[i] = rotate(x[i-1], y[i-1], center[0], center[1], dtheta)
		theta = theta + dtheta

	# generate a plot
	plt.figure(figsize=(10,6))
        plt.plot(x, -y,'k-',label="$z_t=\ %.1f,\\,z_1=\ %.1f,\\,\\theta_1=\ %.2f$" % (yt, y[0], theta0))
        plt.axis('equal')
	plt.title("Flight path for $C$ = %.3f" % C)
        plt.xlabel("$x$", fontsize=16)
	plt.ylabel("$z$", fontsize=16)
	plt.legend()
        plt.show()



