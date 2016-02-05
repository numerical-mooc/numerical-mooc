# 
# Runge-Kutta 4 elemental evaluation
# ==================================
#
# by Alberto Costa Nogueira Jr. (Matlab and Python versions)
#    Renato Cantao (Python version)
#
from simulation_data import BasisType
from local_matrices import local_mass, local_stiffness
from flux import Fluxes
import numpy

def eval_k(sim_data, quad_data, basis, mesh, phi, ic, t):
    nldof = sim_data.n_local_dof()
    Nd = sim_data.n_global_dof() # Total number of dofs
    Nm = Nd+nldof                # One extra element
    Np = Nm+nldof                # Left and right ghosts

    # Allocates local u vector
    u_t = numpy.zeros([Np, 2])      # u evaluated at time steps t and t+dt

    # Gets u from previous stage of RK4
    u_t[nldof:Nm, 0] = phi[0:Nd]

    # Applies Dirichlet BC on u
    if sim_data.basis_type == BasisType.MODAL_ORTHOGONAL:
        u_t[0, 0] = -ic(2.0*numpy.pi*t)
    else:
        u_t[nldof-1, 0] = -ic(2.0*numpy.pi*t)

    # Applies Neumann BC on u (u_ghost2 = u_elementK)
    # du/dx(x_bound) = 0 -> (u_elementK - u_ghost)/dx = 0 -> u_ghost = u_elementK
    u_t[Nm:Np, 0] = u_t[Nd:Nm, 0]     # right side of the domain

    # Constants
    a = numpy.pi
    alpha = 0.0

    # Gets Mass, Stiffness and Flux matrices
    # Note that we multiply S by 2*a
    M = local_mass(quad_data, basis)
    S = 2*a*local_stiffness(quad_data, basis)
    flux = Fluxes(sim_data)
    
    # For performance reasons, we combine the matrices previously
    T = S.T-a*((2.0-alpha)*flux.FR-alpha*flux.FL)

    # Loop over total number of elements
    for i in range(1, sim_data.n_elements+1):
        idx = numpy.arange(nldof*i, nldof*(i+1))

        u_t[idx, 1] = numpy.linalg.solve(M, (T.dot(u_t[idx, 0]) - \
            a*alpha*flux.FRp1.dot(u_t[idx+nldof, 0]) + \
            a*(2.0-alpha)*flux.FLm1.dot(u_t[idx-nldof, 0]))/mesh.J[i-1])

    return u_t[nldof:Nm, 1]

#-- eval_k.py ------------------------------------------------------------------
