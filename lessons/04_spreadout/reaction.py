import numpy
from matplotlib import pyplot
import matplotlib.cm as cm
from matplotlib import animation

n = 192

Du, Dv, F, k = 0.00016, 0.00008, 0.035, 0.065 # Bacteria 1
dh = 5/(n-1)
T = 8000
dt = .9 * dh**2 / (4*max(Du,Dv))
nt = int(T/dt)
nt_save = int(nt/100)
print(dt, dh, nt)

x=numpy.arange(0,5,dh)
y=numpy.arange(0,5,dh)
mx, my = numpy.meshgrid(x,y)

uvinitial = numpy.load('./data/uvinitial.npz')
U = uvinitial['U']
V = uvinitial['V']


# For eventual implicit approach
# def generateMatrix(N, sigma):
#     pass
#
# def generateRHS(T, sigma):
#     pass
# def CrankNicolson(T, A, nt, sigma):
#     pass
# def map_1Dto2D(nx,ny,T_1D, T_bc):
#     pass

# Explicit methodology

def plot(U,V):
    fig = pyplot.figure(figsize=(8,5))
    pyplot.subplot(121)
    pyplot.imshow(U, cmap = cm.RdBu)
    pyplot.xticks([]), pyplot.yticks([]);
    pyplot.subplot(122)
    pyplot.imshow(V, cmap = cm.RdBu)
    pyplot.xticks([]), pyplot.yticks([]);
    pyplot.show()

def ftcs(U, V, nt, Du, Dv, F, k, dt, dh):
    for n in range(nt):
        Un = U.copy()
        Vn = V.copy()
        U[1:-1,1:-1] = Un[1:-1,1:-1] + dt*Du/dh**2 *\
            (Un[2:,1:-1] - 4*Un[1:-1,1:-1] + Un[:-2,1:-1] +\
             Un[1:-1,2:] + Un[1:-1,:-2]) -\
             dt * Un[1:-1,1:-1] * Vn[1:-1,1:-1]**2 +\
             dt * F*(1-Un[1:-1,1:-1])
        V[1:-1,1:-1] = Vn[1:-1,1:-1] + dt*Dv/dh**2 *\
             (Vn[2:,1:-1] - 4*Vn[1:-1,1:-1] + Vn[:-2,1:-1] +\
              Vn[1:-1,2:] + Vn[1:-1,:-2]) +\
              dt * Un[1:-1,1:-1] * Vn[1:-1,1:-1]**2 -\
              dt * (F+k)*Vn[1:-1,1:-1]

        # Enforce Neumann BCs
        U[-1,:] = U[-2,:]
        U[:,-1] = U[:,-2]
        U[0,:] = U[1,:]
        U[:,0] = U[:,1]
        V[-1,:] = V[-2,:]
        V[:,-1] = V[:,-2]
        V[0,:] = V[1,:]
        V[:,0] = V[:,1]

    return U, V

U_time = numpy.zeros((n, n, nt_save))
V_time = numpy.zeros((n, n, nt_save))
U_time[:,:,0]=U
V_time[:,:,0]=V
for n in range(1,nt-1):
    U, V = ftcs(U, V, 2, Du, Dv, F, k, dt, dh)
    if n % 100 == 0:
        U_time[:,:,n/100] = U
        V_time[:,:,n/100] = V

print(U[100,::40])

fig = pyplot.figure()
im = pyplot.imshow(U, cmap = cm.RdBu)

def updatefig(data):
    im.set_array(U_time[:,:,data])
    return [im]


anim = animation.FuncAnimation(fig, updatefig, frames=U_time.shape[2], interval=30, repeat=True,repeat_delay=1000, blit=False)
anim.save('diffusion.mp4', fps=15)
pyplot.show()
