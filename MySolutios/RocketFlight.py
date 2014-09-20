##### Mohammed Attya for #numericalMooc
import numpy
##### Data #####
ms = 50.0                         #the weight of the rocket shell
g = 9.81                          #gravity
rho = 1.091                       #the average air density
r = 0.5                           #radius of cross section of the rocket
a = numpy.pi * r ** 2             #cross sectional area of the rocket
ve = 325.0                        #the exhaust speed
cd = 0.15                         #the drag coefficient
mpo = 100.0                       #the initial weight of the rocket propellant
mpd = 20.0                        #the time-varying burn rate
time = 5                          #time of burning
dt = 0.1
v = numpy.zeros(time/dt)      #speed of rocket
h = numpy.zeros(time/dt)

##### up to 5 sec.
for i in range(len(v)-1):
	mp = mpo - mpd * dt * i
	v[i+1] = dt *(-1 * g +(mpd * ve - 0.5 * rho * a * cd * v[i]**2)/(ms + mp)) + v[i]
	h[i+1] = h[i] + (v[i+1] * dt)
	print('velocity ' + ' ' + str(v[i]) + ' height ' + ' ' + str(h[i]))
print('-----------------------------------------')

while v[i] != 0 :
	s = v[i] - g * dt
	v = numpy.append(v, s)
	time = time + dt
	if time == 20:
		break
print(v)
print("time = ", time)