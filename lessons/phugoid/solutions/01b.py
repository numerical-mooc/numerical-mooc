U = np.array([theta0,omega0])
mu = 0.5
T = 10.0
dt = 0.01
N = int(T/dt)
t = np.linspace(0,T,N+1)

theta = np.zeros(N+1)
theta[0] = U[0]

for n in range(N):
    U = Euler_step(U,dt)
    theta[n+1] = U[0]
    
plt.plot(t,theta,'-ok');
plt.hold(True)

gamma = np.sqrt(1.-(mu**2)/4.)
B = theta0
C = 0.5*theta0*mu/gamma
theta_exact = np.exp(-0.5*mu*t)*(B*np.cos(gamma*t) + C*np.sin(gamma*t))
plt.plot(t,theta_exact,'-r',lw=2);
