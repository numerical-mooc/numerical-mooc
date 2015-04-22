import sys
import math

# Global Variables (frowned upon, I know, but useful here for constants)
# h is altitude of rocket
m_s = 50.0              # weight of rocket shell [kg]
g = 9.81                # gravity [m/s^2] 
rho = 1.091             # constant average air density [kg/m^3] 

r = 0.5                 # radius of rocket [m]
area = math.pi*r*r      # cross sectional area of rocket [m^2]
v_exit = 325.0          # exhaust speed [m/s]
C_D = 0.15              # drag coefficient [unitless]
m_p_0 = 100.0           # initial weight of rocket propellant at t=0 [kg]

# Equations
# dh/dt = v
# (m_s + m_p)*(dv/dt) = (-m_s + m_p)*g + m_p_dot * ve - 0.5*rho*v*abs(v)*A*CD
# m_p = m_p_0 - int((m_p_dot)*dTau, 0, t)
# m_p_dot = propellant burn rate  = 20 [kg/s] from t=0 to t=5, 0 after

# Use Euler's method, detal t=0.1s, find altitude and velocity of rocket from 
# from launch until crashdown

# Calculates the change of mass at this point in time
# param  t  the point in time inquired about [s]
# return    change in mass at that moment in time [kg/s]
def CalcMPDot(t):
    if (t<=5.0) :
        return 20.0
    else :
        return 0.0

# Integrate m_p_dot through t to get m_p_loss
# although the current loss rate is linear, having
# this as a function makes this more extensible going forward
# param  tlower  point in time inquired about [s]
# param  tupper  upper bound in time
# param  dt  timestep [s]
def CalcMPLoss(tlower, tupper, dt):
    mp_loss = 0.0
    t_calc = tlower
    while (t_calc <= tupper):
        mp_loss += dt * CalcMPDot(t_calc)
        t_calc += dt
    return mp_loss

# Calculate the remaining mass of the propellant
# param  tstart  start time for integration [s]
# param  tcurr   current point in time [s]
# param dt  timestep [s]
def CalcMP(tstart, tcurr,dt):
    return max( m_p_0 - CalcMPLoss(tstart,tcurr,dt), 0.0)

def CalcVelocityStep(MTot, MPDot, Vel):
    term1 = 1.0/MTot
    term2 = -MTot*g
    term3 = MPDot*v_exit
    term4 = 0.5*rho*Vel*math.fabs(Vel)*area*C_D
    vStep = term1*(term2+term3-term4)
    return vStep

def Solver():
    # solve the primary function
    Velocity = 0.0      # Velocity [m/s]
    dt = 0.1            # Timestep [0.1]
    height = 0.0        # Height of the rocket [m]
    t_solve = 60.
    t=0.

    # Print parameters
    MPDot = 0.0         # Change in Mass of propellant [kg]
    MProp = 0.0         # mass of the Propellant [kg]
    MTot  = 0.0         # Total Mass [kg]
    VStep = 0.0         # Velocity step [m/s]

    # - Recordkeeping parameters
    VMax = 0.0          # Maximum speed of the rocket [m/s]
    VMaxT = 0.0         # Time of maximum speed  [s]
    VMaxH = 0.0         # Height at maximum velocity [m]
    HMax = 0.0          # Maximum height of the rocket [m]
    HMaxT = 0.0         # Time of Maximum height [s]
    HMaxV = 0.0         # Velocity at maximum height [m/s]

    T_impact = 0.0      # Time of impact [s]
    V_impact = 0.0      # Velocity of impact [s]
    bHasImpacted = False    # Flag indicating that we've impacted the ground

    print('t \t MPdot \t MProp \t MTot \t VStep \t Vel \t height')

    # time loop
    while (t <= t_solve):
        t += dt                     # Increment timestep
        MPDot = CalcMPDot(t)
        MProp = CalcMP(0.1, t, dt)
        MTot = (m_s + MProp)
        VStep = CalcVelocityStep(MTot, MPDot, Velocity)
        Velocity = Velocity + dt*VStep
        
        print('%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t' % (t,MPDot,MProp,MTot,VStep,Velocity,height))

        if(Velocity > VMax):
            VMax = Velocity
            VMaxT = t
            VMaxH = height

        height += dt * Velocity
        if(height > HMax):
            HMax = height
            HMaxT = t
            HMaxV = Velocity

        if(height <= 0.0):
            bHasImpacted = True
            T_impact = t
            V_impact = Velocity
            break           # No need to continue since we've got impact


    print('At t=%.2f s, Rocket has following properties:' % t)
    print('\t Altitude:\t\t%.2f [m]' % height)
    print('\t Total Mass \t\t%.2f [kg]' % MTot)
    print('\t Propellant Mass \t%.2f [kg]' % MProp)
    print('\t Velocity \t\t%.2f [m/s]' % Velocity)
    print('\t Velocity Step\t\t%.2f [m/s]' % VStep)
    print('\t Max Velocity Attained\t%.2f [m/s] at t=%.2f at h=%.2f' % (VMax, VMaxT, VMaxH))
    print('\t MaxAltitude:\t\t%.2f [m] at t=%.2f at V=%.2f' % (HMax, HMaxT, HMaxV))
    print('')
    if(bHasImpacted):
        print('Rocket has impacted the ground!')
        print('\t Time \t%.2f [s]' % T_impact)
        print('\t Velocity\t%.2f[m/s]' % V_impact)
    else:
        print('Rocket did not impact the ground!')

def main(argv):
    # Primary main function
    Solver()
    pass

if __name__ == "__main__":
    main(sys.argv)