def f(U):
    return np.array( [U[1],
                      -U[0]-mu*U[1]] )

def Euler_step(U,dt):
    return U + dt*f(U)

theta0 = np.pi/4
omega0 = 0.
U = np.array([theta0,omega0])

T = 20.0
dt = 0.01
N = int(T/dt)
t = np.linspace(0,T,N+1)

theta = np.zeros(N+1)
theta[0] = U[0]

for n in range(N):
    U = Euler_step(U,dt)
    theta[n+1] = U[0]
    
plt.plot(t,theta);
