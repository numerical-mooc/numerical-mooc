# 
# Projection of initial condition
# ===============================
#
# by Alberto Costa Nogueira Jr. (Matlab and Python versions)
#    Renato Cantao (Python version)
#
import numpy

def ic_projection(quad_data, basis, fxi, M):
    """Projects the initial condition into polynomial space.

    Arguments:
        sim_data - SimulationData object
        quad_data - Quadrature points and weights
        basis - Basis and respective derivatives
        fxi - Function to be projected
        M - Elemental mass matrix
        is_diagonal - Hint to the solver. Diagonal matrices are much faster to
            solve

    Returns:
        Polynomial coefficients corresponding to fxi
    """
    return numpy.linalg.solve(M, numpy.dot(quad_data.w*basis.psi.T, fxi))
