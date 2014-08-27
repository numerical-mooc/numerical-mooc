import numpy as np
import matplotlib.pyplot as plt

# use the sign convention and formulae provided by Lanchester (1909)

# calculate the radius of curvature of the flight path at any point
def radius_of_curvature(y, yt, C):
	return 2./(C*(1./y)**1.5 - 2./3./yt)

# given the coordinates of a point, the center around which it much revolve,
# and the angle of rotation, calculate the new position of the point
def rotate(x, y, xCenter, yCenter, angle):
	dx = x - xCenter
	dy = y - yCenter
	xNew = dx*np.cos(angle) - dy*np.sin(angle)
	yNew = dx*np.sin(angle) + dy*np.cos(angle)
	return xCenter + xNew, yCenter + yNew

# plot the flight path. The inputs are the trim height and the initial position 
# and orientation of the aircraft
def plot_flight_path(yt, y0, theta0, case_name = 'dummy'):	
    # arrays to store the coordinates of the flight path
	N = 2000
	y = np.zeros(N)
	x = np.zeros(N)

	# set initial conditions
	y[0] = y0
	x[0] = 0.
	theta = theta0

	# calculate the constant C
	C = np.sqrt(y[0])*(np.cos(theta) - y[0]/yt/3.)

	# incremental distance along the flight path
	ds = 1.

	# obtain the curve coordinates
	for i in xrange(1,N):
		normal = np.array([np.cos(theta+np.pi/2.), np.sin(theta+np.pi/2.)])
		R = radius_of_curvature(y[i-1], yt, C)
		center = np.array([x[i-1]+normal[0]*R, y[i-1]+normal[1]*R])
		dtheta = ds/R
		x[i], y[i] = rotate(x[i-1], y[i-1], center[0], center[1], dtheta)
		theta = theta + dtheta

	# generate a plot
	plt.ion()
	plt.plot(x, -y, label="$z_t=%.1f,\\,z_1=%.1f,\\,\\theta_1=%.2f$" % (yt, y[0], theta0))
	plt.title("Flight path for C = %.4f" % C)
	plt.ylabel("$z$")
#	plt.axis([-100, 1000, -300, 50])
	plt.legend()

