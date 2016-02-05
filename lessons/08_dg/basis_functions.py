#
# Basis functions and respective derivatives
#
# by Alberto Costa Nogueira Jr. (Matlab and Python versions)
#    Renato Cantao (Python version)
#
import numpy
from sys import float_info
from math import fabs, sqrt
from jacobi_p import jacobi_p
from djacobi_p import djacobi_p, d_pq, d2_pq
from jacobi_roots import jacobi_roots
from simulation_data import QuadratureNodes, BasisType

def gll_nodes(n_local_dof):
    """Gauss-Legendre-Lobatto auxiliar points.
    
    Parameters
    ----------
    n_local_dof
        Per-element number of degrees of freedom
    """
    if n_local_dof < 2:
        raise AssertionError("Local degress of freedom must be >= 2!")

    # Setting GLL nodes
    alpha = 0.0
    beta  = 0.0

    xj = numpy.empty(n_local_dof)

    # GLL points are the roots of a Jacobi polynomial with alpha = beta = 1,
    # plus the interval extrema, -1 and 1.
    xj[0] = -1.0
    xj[1:-1] = jacobi_roots(n_local_dof-2, alpha+1.0, beta+1.0)
    xj[-1] = 1.0

    return xj

def lagrange(n_local_dof, xi, xj):
    """Lagrange basis function.

    Parameters
    ----------
    n_local_dof
        Number of local degrees of freedom
    xi
        Distribution of integration points on the element defining the
        Lagrangian basis
    xj
        Points where we evaluate the basis
    """
    # Number of Lagrange basis functions
    Q   = n_local_dof
    QQ1 = Q*(Q-1)

    # Number of evaluation points
    npts = xi.shape[0]

    # Allocates matrix to store Lagrange basis evaluated at npts points
    Hj = numpy.ones([npts, Q])
    Hj[:, 0] = ((-1.0)**(Q-1)/QQ1)*(xi-1.0)*(0.5*Q*jacobi_p(xi, Q-2, 1.0, 1.0))
    Hj[:,-1] = (1.0/QQ1)*(xi+1.0)*(0.5*Q*jacobi_p(xi, Q-2, 1.0, 1.0))
    
    Lp  =  jacobi_p(xj, Q-1, 0.0, 0.0)
    DLp = djacobi_p(xi, Q-1, 0.0, 0.0)

    for j in range(1, Q-1):   # from the second to the second-last column
        for i in range(0, npts):
            if fabs(xi[i]-xj[j]) > float_info.epsilon:
                Hj[i, j] = (xi[i]**2-1.0)*DLp[i]/(QQ1*Lp[j]*(xi[i]-xj[j]))

    return Hj

def bubble_basis(n_local_dof, xi):
    """Modal bubble functions.
    n_local_dof
        Number of local degrees of freedom
    xi
        Distribution of integration points on the element
    """
    # Number of bubble basis functions
    Q = n_local_dof

    # Number of evaluation points
    npts = xi.shape[0]

    # Allocates matrix to store Lagrange basis evaluated at npts points
    Bj = numpy.empty([npts, Q])
    
    # Boundary nodal basis functions (necessary to enforce C^(0) continuity)
    Bj[:, 0] = 0.5*(1.0-xi)
    Bj[:,-1] = 0.5*(1.0+xi)

    # Bubble modes
    for j in range(1, Q-1):
        Lj   = jacobi_p(xi, j+1, 0.0, 0.0)
        Ljm2 = jacobi_p(xi, j-1, 0.0, 0.0)
        Bj[:, j] = (Lj-Ljm2)/sqrt(2.0*(2.0*j+1.0))

    return Bj
    
def legendre_basis(n_local_dof, xi):
    """Legendre basis functions.
    n_local_dof
        Number of local degrees of freedom
    xi
        Distribution of integration points on the element
    """
    # Number of basis functions
    Q = n_local_dof

    # Number of evaluation points
    npts = xi.shape[0]

    # Allocates matrix to store Lagrange basis evaluated at npts points
    Lj = numpy.empty([npts, Q])
    
    # Legendre basis
    for j in range(0, Q):
        Lj[:, j] = jacobi_p(xi, j, 0.0, 0.0)

    return Lj
    
def orthonormal_legendre_basis(n_local_dof, xi):
    """Legendre basis functions.
    n_local_dof
        Number of local degrees of freedom
    xi
        Distribution of integration points on the element
    """
    # Number of basis functions
    Q = n_local_dof

    # Number of evaluation points
    npts = xi.shape[0]

    # Allocates matrix to store Lagrange basis evaluated at npts points
    Lj = numpy.empty([npts, Q])
    
    # Legendre basis with the orthonormalization factor
    for j in range(0, Q):
        Lj[:, j] = jacobi_p(xi, j, 0.0, 0.0)/numpy.sqrt(2.0/(2.0*j+1.0))

    return Lj
    
class BasisFunctions:
    """Basis functions and derivatives on quadrature points."""
    def __init__(self, sim_data, gauss_quad):
        """
        Parameters
        ----------
        sim_data
            SimulationData object
        """
        n_local_dof = sim_data.n_local_dof()

        # Constructing the basis functions PHI
        if sim_data.basis_type == BasisType.NODAL:
            xj = gll_nodes(n_local_dof)
            self.psi = lagrange(n_local_dof, gauss_quad.xi, xj)
        elif sim_data.basis_type == BasisType.MODAL:
            self.psi = bubble_basis(n_local_dof, gauss_quad.xi)
        elif sim_data.basis_type == BasisType.MODAL_ORTHOGONAL:
            self.psi = legendre_basis(n_local_dof, gauss_quad.xi)
        elif sim_data.basis_type == BasisType.MODAL_ORTHONORMAL:
            self.psi = orthonormal_legendre_basis(n_local_dof, gauss_quad.xi)
        else:
            raise AssertionError( "Wrong basis type!\n" )

        # Now we construct the derivative of the basis functions, DPHI/DX
        nip = sim_data.nip()

        self.D = numpy.zeros([nip, nip])

        if nip > 1:
            dp  =  d_pq(gauss_quad.xi, nip, 0.0, 0.0, sim_data.node_dist)
            dp2 = d2_pq(gauss_quad.xi, nip, 0.0, 0.0, sim_data.node_dist)
        
            for i in range(0, nip):
                for j in range(0, nip):
                    # Never do "ifs" inside loops! Just for pedagogic reasons.
                    if i == j:
                        self.D[i, j] = dp2[i]/(2.0*dp[i])
                    else:
                        dx = gauss_quad.xi[i] - gauss_quad.xi[j]
                        self.D[i, j] = dp[i]/(dp[j]*dx)

        self.dpsi = self.D.dot(self.psi)

#-- basis_functions.py ---------------------------------------------------------
