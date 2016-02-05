# 
# Runge-Kutta 4 elemental evaluation (wave equation version)
# ==========================================================
#
# by Alberto Costa Nogueira Jr. (Matlab and Python versions)
#    Renato Cantao (Python version)
#
from simulation_data import BasisType
from local_matrices import local_mass, local_stiffness, stress_stiffness
from flux import Fluxes
import numpy

def eval_k_wave(sim_data, quad_data, basis, mesh, mat_prop, phi, s, t):
    ng = sim_data.n_global_dof()
    nl = sim_data.n_local_dof()
    K  = sim_data.n_elements   # saving some typing...

    # Allocates local vectors v and sigma
    v_t = numpy.zeros([(K+2)*nl, 2])     # size: K elements + 1 ghost
    sigma_t = numpy.zeros(v_t.shape) # size: K elements + 1 ghost

    # Gets v and sigma from previous stage of RK4
    v_t[nl:(K+1)*nl, 0] = phi[ng:2*ng]
    sigma_t[nl:(K+1)*nl,0] = phi[2*ng:3*ng]

    # Applies Neumann BC on v (v_ghost = v_element1)
    # d/dx v(x_bound) = 0 -> (v_element1 - v_ghost)/delta_x = 0 -> v_ghost = v_element1
    v_t[0:nl, 0] = v_t[nl:2*nl, 0]            # left side of the domain
    v_t[ng+nl:ng+2*nl, 0] = v_t[ng:ng+nl, 0]  # right side of the domain
 
    # Gets Mass, Stiffness and Flux matrices
    # Note that we multiply S by 2*a
    M = local_mass(quad_data, basis)
    S = local_stiffness(quad_data, basis)
    flux = Fluxes(sim_data)

    # Loop over total number of elements
    for i in range(1, sim_data.n_elements+1):
        Ss, Ssm = stress_stiffness(quad_data, basis, mat_prop, i-1)

        idx = numpy.arange(nl*i, nl*(i+1))
        m1 = 0.5*flux.FRp1.dot(sigma_t[idx+nl, 0]+numpy.sqrt(mat_prop.rho[i-1]*mat_prop.mub[nl-1, i])*v_t[idx+nl, 0] )
        m2 = 0.5*flux.FR.dot(sigma_t[idx, 0]-numpy.sqrt(mat_prop.rho[i-1]*mat_prop.mub[nl-1, i])*v_t[idx, 0])
        m3 = 0.5*flux.FL.dot(sigma_t[idx, 0]+numpy.sqrt(mat_prop.rho[i-1]*mat_prop.mub[0, i])*v_t[idx, 0])
        m4 = 0.5*flux.FLm1.dot(sigma_t[idx-nl, 0]-numpy.sqrt(mat_prop.rho[i-1]*mat_prop.mub[0, i])*v_t[idx-nl, 0])

        tmp = (s[idx-nl]-S.T.dot(sigma_t[idx, 0])+m1+m2-m3-m4)/(mesh.J[i-1]*mat_prop.rho[i-1])

        v_t[idx, 1] = numpy.linalg.solve(M, \
           tmp )

        m1 = 0.5*flux.FRp1.dot(v_t[idx+nl, 0]+(mat_prop.rho[i-1]*mat_prop.mub[nl-1, i])**(-0.5)*sigma_t[idx+nl, 0] )
        m2 = 0.5*flux.FR.dot(v_t[idx, 0]-(mat_prop.rho[i-1]*mat_prop.mub[nl-1, i])**(-0.5)*sigma_t[idx, 0])
        m3 = 0.5*flux.FL.dot(v_t[idx, 0]+(mat_prop.rho[i-1]*mat_prop.mub[0, i])**(-0.5)*sigma_t[idx, 0])
        m4 = 0.5*flux.FLm1.dot(v_t[idx-nl, 0]-(mat_prop.rho[i-1]*mat_prop.mub[0, i])**(-0.5)*sigma_t[idx-nl, 0])

        tmp = (-Ss.dot(v_t[idx, 0])-mesh.J[i-1]*Ssm.dot(v_t[idx, 0])+ \
                mat_prop.mub[nl-1, i]*(m1+m2)+mat_prop.mub[0, i]*(-m3-m4))/mesh.J[i-1]
        sigma_t[idx, 1] = numpy.linalg.solve(M,  tmp)

    # Assigns local vectors u, v and sigma to the new global vector phi
    ki = numpy.zeros(3*ng)

    ki[0:ng]      = v_t[nl:(K+1)*nl, 0]
    ki[ng:2*ng]   = v_t[nl:(K+1)*nl, 1]
    ki[2*ng:3*ng] = sigma_t[nl:(K+1)*nl, 1]

    return ki

#-- eval_k_wave.py -------------------------------------------------------------
