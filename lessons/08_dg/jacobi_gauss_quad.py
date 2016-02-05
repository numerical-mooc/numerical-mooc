#
# Points and weights for Gaussian quadrature
#
# by Alberto Costa Nogueira Jr. (Matlab and Python versions)
#    Renato Cantao (Python version)
#
import numpy
from math import gamma
from jacobi_p import jacobi_p
from djacobi_p import djacobi_p
from jacobi_roots import jacobi_roots
from simulation_data import QuadratureNodes

class JacobiGaussQuad:
    """Points and weights for Gaussian quadrature based on Jacobi polynomials"""
    def __init__(self, sim_data):
        # Sets parameters to obtain quadrature points from Legendre polynomials
        # Legendre == Jacobi(0,0)
        alpha = 0.0
        beta  = 0.0
        nip = sim_data.nip()

        # Case 1: Gauss-Legendre quadrature
        if sim_data.node_dist == QuadratureNodes.GL:
            self.xi, self.w = self._gl(nip, alpha, beta)
        # Case 2: Gauss-Legendre-Lobato quadrature
        elif sim_data.node_dist == QuadratureNodes.GLL:
            self.xi, self.w = self._gll(nip, alpha, beta)
        else:
            raise AssertionError("Unknown quadrature type!")

    # Case 1: Gauss-Legendre quadrature
    def _gl(self, nip, alpha, beta):
        xi = jacobi_roots(nip, alpha, beta)

        C1 = (2.0**(alpha+beta+1.0))*gamma(alpha+nip+1.0)*gamma(beta+nip+1.0)
        C2 = gamma(nip+1.0)*gamma(alpha+beta+nip+1.0)*(1.0-xi**2 )

        DPm = djacobi_p(xi, nip, alpha, beta)

        w = C1*DPm**(-2)/C2

        return xi, w

    # Case 2: Gauss-Legendre-Lobato quadrature
    def _gll(self, nip, alpha, beta):
        r = jacobi_roots(nip-2, alpha+1.0, beta+1.0)
        xi = numpy.empty(r.shape[0]+2)
        xi[0] = -1.0
        xi[1:-1] = r
        xi[-1] = 1.0

        C1 = (2.0**(alpha+beta+1.0))*gamma(alpha+nip)*gamma(beta+nip)
        C2 = (nip-1)*gamma(nip)*gamma(alpha+beta+nip+1.0)

        Pm = jacobi_p(xi, nip-1, alpha, beta)

        w = C1*Pm**(-2)/C2

        w[ 0] = w[ 0]*(beta+1.0)
        w[-1] = w[-1]*(alpha+1.0)

        return xi, w

    def n(self):
        """Number of integration points / weights."""
        return self.xi.shape[0]

#-- jacobi_gauss_quad.py -------------------------------------------------------
