# 
# Local mass and stiffness matrices
# =================================
#
# by Alberto Costa Nogueira Jr. (Matlab and Python versions)
#    Renato Cantao (Python version)
#
import numpy

def local_mass(quad_data, basis):
    """Constructs the elemental mass matrix

    Arguments:
        quad_data - Quadrature points and weights
        basis - Basis and respective derivatives

    Returns:
        Mass matrix M, where m_ij = \int_k psi_i psi_j
    """
    return numpy.dot(quad_data.w*basis.psi.T, basis.psi)

def local_mass_diagonal(quad_data, basis):
    """Constructs the elemental mass matrix, diagonal version

    Arguments:
        quad_data - Quadrature points and weights
        basis - Basis and respective derivatives

    Returns:
        Mass matrix M, where m_ii = \int_k psi_i psi_i
    """
    return numpy.sum(quad_data.w*basis.psi.T**2, axis=1)

def local_stiffness(quad_data, basis):
    """Constructs the elemental stiffness matrix

    Arguments:
        quad_data - Quadrature points and weights
        basis - Basis and respective derivatives

    Returns:
        Stiffness matrix S, where s_ij = \int_k psi_i Dpsi_j/dx
    """
    return numpy.dot(quad_data.w*basis.psi.T, basis.dpsi)

#-- local_matrices.py ----------------------------------------------------------
