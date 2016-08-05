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
dt = 0.001
v = numpy.zeros(time/dt)      #speed of rocket
h = numpy.zeros(time/dt)

##### up to 5 sec.
for i in range(len(v)-1):
	mp = mpo - mpd * dt * i
	v[i+1] = dt *(-1 * g +(mpd * ve - 0.5 * rho * a * cd * v[i]**2)/(ms + mp)) + v[i]
	h[i+1] = h[i] + (v[i+1] * dt)

print('Max velocity ', v[i])
print('Height ', h[i])


# the fuel finish
s = list() #list of velocity after the fuel finished
s.append(v[i])
hh = h[i]  #altitude after the fuel finished
i = 1
mp, mpd = 0, 0

while s[i-1] > -0.000000001 :
	s.append(dt *(-1 * g -(0.5*rho * a * cd * s[i-1]**2)/ ms) + s[i-1])
	time = time + dt
	hh = hh + s[i] * dt
	i += 1

print("time = ", time)
print('Max height', hh)

#free fall
vel0 = 0 #velocity of free fall

while hh > -0.00000001:
	vel1 = dt *(1 * g -(0.5*rho * a * cd * vel0**2)/ ms) + vel0
	time = time + dt
	hh = hh - vel0 * dt
	vel0 = vel1

print('time of impact ', time)
print('velocity of Impact', vel1)
