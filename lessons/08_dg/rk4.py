# 
# Runge-Kutta 4 steps method
# ==========================
#
# by Alberto Costa Nogueira Jr. (Matlab and Python versions)
#    Renato Cantao (Python version)
#
from simulation_data import BasisType
from eval_k import eval_k

def RK4(sim_data, quad_data, basis, mesh, tstep, t, dt, ic, u, phi):
    """Runge-Kutta 4 steps.

    Arguments:
        sim_data - SimulationData object
        quad_data - Quadrature points and weights
        basis - Basis and respectivederivatives
        mesh - 1D Finite Elements mesh
        tstep - present time step (integer)
        t - simulation time
        dt - delta t
        ic - initial condition function
        u - solution
        phi -

    Returns:
        A step of the RK4 method
    """
    ngdof = sim_data.n_global_dof()

    # RK4
    k1 = eval_k(sim_data, quad_data, basis, mesh, phi, ic, t)
    k2 = eval_k(sim_data, quad_data, basis, mesh, phi+0.5*dt*k1, ic, t)
    k3 = eval_k(sim_data, quad_data, basis, mesh, phi+0.5*dt*k2, ic, t)
    k4 = eval_k(sim_data, quad_data, basis, mesh, phi+dt*k3, ic, t)
    
    phi = phi+dt*(k1+2.0*k2+2.0*k3+k4)/6.0

    # Recovers displacement solution u for modal type basis
    if sim_data.basis_type == BasisType.NODAL:
        u[:, tstep] = phi[0:ngdof]
    else:
        nip = sim_data.nip()
        nldof = sim_data.n_local_dof()

        u_hat = phi[0:ngdof]

        for k in range(0, sim_data.n_elements):
            u[nip*k:nip*(k+1), tstep] = \
                u_hat[nldof*k:nldof*(k+1)].dot(basis.psi.T)

    return (u, phi)

#-- rk4.py ---------------------------------------------------------------------
