import numpy as np
import matplotlib.pyplot as plt

gamma = 1.4
nx=81
dx = .25
dt=.0002
gamma = 1.4
gammasub1 = gamma-1
nt = 0.001/dt
print(nt)
x = np.linspace(-10, 10, nx)
print(x[490:510])

def calculate_flux(u):
    """ Calculate flux in terms of parts of the state vector u.
    The state vector u is
    [density, velocity*density, density*specific total energy].

    Assumes gammasub1 is available from the global scope.
    """
    u1, u2, u3 = u
    u22u1 = u2*u2/u1
    return np.array([u2, u2**2/u1 + gammasub1*(u3-0.5*u22u1), u3+gammasub1*(u3-0.5*u22u1)*u2/u1])

def Sod_initial_conditions():
    # left
    rho=1.
    u=0.
    p=100.e3
    e=p/(gammasub1*rho)
    e_t=e+u**2/2.
    ICL = np.array([rho, rho*u, rho*e_t])
    rho=0.125
    u=0.
    p=10.e3
    e=p/(gammasub1*rho)
    e_t=e+u**2/2.
    ICR = np.array([rho, rho*u, rho*e_t])
    return ICL, ICR

def exercise_initial_conditions(nx, icl, icr):
    result = np.ones((nx,3))*icr
    result[:nx/2,:]=icl
    return result

ICL, ICR = Sod_initial_conditions()
print(ICL, ICR)
u_initial=exercise_initial_conditions(nx, ICL, ICR)

def plot_solution(u, x):
    row1=u[:,0]
    row2=u[:,1]/row1
    row3=gammasub1*(u[:,2] - 0.5*row2**2/row1)
    plt.plot(x,row1, "bo-", label="density")
    plt.plot(x,row2, "ro-", label="velocity")
    plt.plot(x,row3, "go-", label="pressure")
    plt.legend()
    plt.grid()
    plt.show()
def richtmeyer_solution(nx, nt, dt, dx, u_initial):
    u = np.empty((nx, 3, nt))
    u[:,:,0] = u_initial
    """
    Pick up here
    """    
    return u
solution = richtmeyer_solution(nx, nt, dt, dx, u_initial)
plot_solution(solution[:,:,0], x)
