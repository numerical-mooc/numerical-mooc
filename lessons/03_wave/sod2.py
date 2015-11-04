import numpy as np
import matplotlib.pyplot as plt
import pdb
gamma = 1.4
nx=81
dx = .25
# dt=.0002
# nt = int(0.001/dt)
dt=.0002
T=0.01
#T=0.001
nt = int(T/dt)+1
print("NT = " + str(nt))
gamma = 1.4
gammasub1 = gamma-1
print(nt)
x = np.linspace(-10, 10, nx)

def calculate_flux(u):
    """ Calculate flux in terms of parts of the state vector u.
    The state vector u is
    [density, velocity*density, density*specific total energy].

    Assumes gammasub1 is available from the global scope.
    """
    u1 = u[:,0]
    u2 = u[:,1]
    u3 = u[:,2]
    u22u1 = u2*u2/u1
    result =  np.vstack((u2, u2**2/u1 + gammasub1*(u3-0.5*u22u1), (u3+gammasub1*(u3-0.5*u22u1))*u2/u1)).T
    return result

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
    # plt.plot(x,row2, "ro-", label="velocity")
    # plt.plot(x,row3, "go-", label="pressure")
    plt.legend()
    plt.grid()
    plt.show()
def answer_solution(u, x):
    row1=u[:,0]
    row2=u[:,1]/row1
    density=row1
    velocity=row2
    pressure=gammasub1*(u[:,2] - 0.5*u[:,1]**2/row1)
    target=(x>2.4)*(x < 2.6)
    # for i, xi in enumerate(x):
    #     print (i, xi, target[i], density[i], velocity[i], pressure[i])
    print(velocity[target], pressure[target], density[target])


def maccormack(nx, nt, dt, dx, u_initial):
    un = np.zeros((nx, 3, nt))
    un[:] = u_initial.copy()
    ustar = u_initial.copy()
    for t in range(1,nt):
        F = calculate_flux(u)
        ustar[:-1] = u[:-1]-dt/dx*(F[1:] - F[:-1])
        Fstar = computeF(ustar)
        un[t,1:]=0.5*(u[1:]+ustar[1:]-dt/dx*(Fstar[1:] - Fstar[:-1]))
        u = un[t].copy()
    return un

def richtmeyer_solution(nx, nt, dt, dx, u_initial):
    print(nt)
    u = np.zeros((nx, 3, nt))
    u[:,:,0] = u_initial
    pdb.set_trace()
    for n in range(1, nt):
        u_i_n=u[:,:,n-1]
        u_i1_n=u_i_n[1:,:]
        u_i0_n=u_i_n[:-1,:]
        u_ihalf_nhalf = 0.5*((u_i1_n+u_i0_n)-dt/dx*(calculate_flux(u_i1_n)-calculate_flux(u_i0_n)))
        u_iminushalf_nhalf = u_ihalf_nhalf[:-1,:]
        u_ihalf_nhalf = u_ihalf_nhalf[1:,:]
        u_i_none = u_i_n[1:-1,:] - dt/dx*(calculate_flux(u_ihalf_nhalf)-calculate_flux(u_iminushalf_nhalf))

        u[1:-1,:,n] = u_i_none
    return u

f = calculate_flux

##second pass
def richtmeyer_solution(nx, nt, dt, dx, u_initial):
    u = np.zeros((nx, 3, nt))
    u[:,:,0] = u_initial
    for n in range(0,nt-1):
        print(n)
        u_n = u[:,:,n].copy()
        shifted_foward = u_n[1:,:]
        trimmed_from_forward = u_n[:-1,:]
        u_half=0.5*(shifted_foward + trimmed_from_forward - dt/dx*(f(shifted_foward)-f(trimmed_from_forward)))
        u_half_shifted_forward=u_half[1:,:]
        u_half_trimmed_from_forward=u_half[:-1,:]
        u_new = u_n
        subtraction =  dt/dx * (f(u_half_shifted_forward)-f(u_half_trimmed_from_forward))
        u_new[1:-1,:] -= subtraction
        u[:,:,n+1]=u_new
    return u

solution = richtmeyer_solution(nx, nt, dt, dx, u_initial)
density = solution[:,0,:]
velocity = solution[:,1,:] / density
energy = solution[:,2,:] / density
# for n in range(1,nt):
#     plot_solution(solution[:,:,n]-solution[:,:,n-1], x)
# for n in range(0,nt):
#     plot_solution(solution[:,:,n], x)

# answer_solution(solution[:,:,-1], x)
import numpy
import matplotlib.pyplot as plt
from matplotlib import animation
from JSAnimation.IPython_display import display_animation
fig = plt.figure();
ax = plt.axes(xlim=(-10,10),ylim=(0,2));
line, = ax.plot([],[], "bo-", lw=2);
def animate(data):
    y = data
    line.set_data(x,y)
    return line,
answer_solution(solution[:,:,-1], x)
anim = animation.FuncAnimation(fig, animate, frames=density.T, interval=10, repeat=False)
plt.show()
