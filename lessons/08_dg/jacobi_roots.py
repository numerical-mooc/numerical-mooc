#
# Roots of Jacobi polynomials with parameters alpha and beta
#
#
# by Alberto Costa Nogueira Jr. (Matlab and Python versions)
#    Renato Cantao (Python version)
#
from math import cos, pi, fabs
from sys import float_info
from jacobi_p import jacobi_p
from djacobi_p import djacobi_p
import numpy

def jacobi_roots(m, alpha = 0.0, beta = 0.0):
    """Polynomial deflation to find the zeros of a Jacobi polynomial."""
    if m == 0:
        raise AssertionError("0-degree Jacobi polynomial detected!")
    elif m == 1:
        return numpy.array([(beta-alpha)/(alpha+beta+2.0)])
    else:
      x = numpy.zeros(m)      # Allocating vector for quadrature points
   
      # Newton-Raphson algorithm with polynomial deflation
      for k in range(0, m):
          # Initial guess: roots of the Chebyshev polynomial of order m
          r = -cos(pi*(2*k+1)/(2*m))
          if k > 0:
              r = 0.5*(r+x[k-1])
              #print("r = %s, x[%i] = %s" % (r, k, x[k]))
          delta = 1.0

          while fabs(delta) > float_info.epsilon:
              s = numpy.sum( 1.0/(r-x[range(0, k)]) )
              Pm  = jacobi_p(r, m, alpha, beta)
              DPm = djacobi_p(r, m, alpha, beta)
              delta = -Pm/(DPm-Pm*s)
              r = r+delta
          
          x[k] = r

    return x

#-- jacobi_roots.py ------------------------------------------------------------
