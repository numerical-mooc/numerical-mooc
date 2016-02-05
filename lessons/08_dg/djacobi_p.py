#
# Jacobi polynomial derivative evaluated at a point or vector
#
# by Alberto Costa Nogueira Jr. (Matlab and Python versions)
#    Renato Cantao (Python version)
#
from numbers import Number
import numpy
from math import gamma
from simulation_data import QuadratureNodes
from jacobi_p import jacobi_p

def djacobi_p(x, m, alpha = 0.0, beta = 0.0):
    """Jacobi polynomial derivative."""
    number_flag = False

    if isinstance(x, Number):
        x = numpy.array([x])
        number_flag = True

    aPb = alpha+beta   # mnemonics: alpha plus beta
    aMb = alpha-beta   # mnemonics: alpha minus beta

    Pn  = numpy.ones(x.shape)
    Pn1 = 0.5*(aMb+(aPb+2.0)*x)
    DPm = numpy.zeros(x.shape)

    if m == 0:
        return DPm
    elif m == 1:
        DPm = 0.5*(aPb+2.0)*Pn
    else:
        idx = (x > -1.0) & (x < 1.0)
        idxm1 = (x == -1.0)
        idxp1 = (x ==  1.0)
 
        # Check if we *really* have at most one x=-1.0 and one x=1.0
        if len(numpy.where(idxm1)) > 1 or len(numpy.where(idxp1)) > 1:
            raise AssertionError("Too much -1.0 or 1.0 on the domain!")

        x_inner   = x[idx]
        DPm_inner = DPm[idx]

        for n in range(1, m+1):
            n1 = n+1.0;
            n2 = 2.0*n;

            facA = gamma(m+alpha+1.0);
            facB = gamma(m+beta+1.0);

            a1n = 2.0*n1*( n1+aPb )*( n2+aPb );
            a2n = ( n2+aPb+1.0 )*aPb*aMb;
            a3n = ( n2+aPb )*( n2+aPb+1.0 )*( n2+aPb+2.0 );
            a4n = 2.0*( n+alpha )*( n+beta )*( n2+aPb+2.0 );

            Pn2 = ( ( a2n+a3n*x )*Pn1-a4n*Pn )/a1n;

            b1n = ( n2+aPb )*( 1.0-x_inner**2 );
            b2n = n*( aMb-( n2+aPb )*x_inner );
            b3n = 2.0*( n+alpha )*( n+beta );

            DPm_inner = ( b2n*Pn1[idx] + b3n*Pn[idx] )/b1n; 

            Pn  = Pn1;
            Pn1 = Pn2;

            DPm[idxm1] = (-1.0)**(m-1)*0.5*(aPb+m+1.0)*facB/(gamma(beta+2.0)*gamma(m));
            DPm[idxp1] = 0.5*(aPb+m+1.0)*facA/(gamma(alpha+2.0)*gamma(m));
            DPm[idx  ] = DPm_inner;

    if number_flag:
        return DPm[0]
    else:
        return DPm

def d_pq(x, m, alpha, beta, node_dist):
    """First derivative of the auxiliar polynomial PQ"""
    number_flag = False

    if isinstance(x, Number):
        x = numpy.array([x])
        number_flag = True

    if node_dist == QuadratureNodes.GL:
        return djacobi_p(x, m, alpha, beta)
    elif node_dist == QuadratureNodes.GLL:
        idx = (x > -1.0) & (x < 1.0)
        idxm1 = (x == -1.0)
        idxp1 = (x ==  1.0)

        # Check if we *really* have at most one x=-1.0 and one x=1.0
        if len(numpy.where(idxm1)) > 1 or len(numpy.where(idxp1)) > 1:
            raise AssertionError("Too much -1.0 or 1.0 on the domain!")

        dp = numpy.empty(x.shape)

        # -1.0 < x < 1.0
        dp[idx] = -2.0*(m-1)*jacobi_p(x[idx], m-1, alpha, beta)

        # x = -1.0
        c = 2.0*(-1.0)**m;
        gamma1 = gamma(m+beta)
        gamma2 = gamma(m-1)
        gamma3 = gamma(beta+2)
        dp[idxm1] = (c*gamma1)/(gamma2*gamma3) 

        # x = 1.0
        c = -2;
        gamma1 = gamma(m+alpha)
        gamma2 = gamma(m-1)
        gamma3 = gamma(alpha+2)
        dp[idxp1] = (c*gamma1)/(gamma2*gamma3)
    else:
        raise AssertionError("Wrong quadrature type!")

    if number_flag:
        return dp[0]
    else:
        return dp
 
def d2_pq(x, m, alpha, beta, node_dist):
    """Second derivative of the auxiliar polynomial PQ"""
    number_flag = False

    if isinstance(x, Number):
        x = numpy.array([x])
        number_flag = True
        
    if node_dist == QuadratureNodes.GL:
        return (alpha-beta+(alpha+beta+2.0)*x)*djacobi_p(x, m, alpha, beta)/(1.0-x**2)
    elif node_dist == QuadratureNodes.GLL:
        idx = (x > -1.0) & (x < 1.0)
        idxm1 = (x == -1.0)
        idxp1 = (x ==  1.0)

        # Check if we *really* have at most one x=-1.0 and one x=1.0
        if len(numpy.where(idxm1)) > 1 or len(numpy.where(idxp1)) > 1:
            raise AssertionError("Too much -1.0 or 1.0 on the domain!")

        # Solution without the boundaries
        x_inner = x[idx]

        dp = numpy.empty(x.shape)

        # -1.0 < x < 1.0
        dp[idx] = (alpha-beta+(alpha+beta)*x_inner)*(-2.0*(m-1))* \
                jacobi_p(x_inner, m-1, alpha, beta)/((1.0-x_inner)*(1.0+x_inner))

        # x = -1.0
        c = (2*(-1.0)**m*(alpha-(m-1)*(m+alpha+beta)))/(beta+2)
        gamma1 = gamma(m+beta)
        gamma2 = gamma(m-1)
        gamma3 = gamma(beta+2)
        dp[idxm1] = (c*gamma1)/(gamma2*gamma3) 

        # x = 1.0
        c = (2.0*(beta-(m-1)*(m+alpha+beta)))/(alpha+2)
        gamma1 = gamma(m+alpha)
        gamma2 = gamma(m-1)
        gamma3 = gamma(alpha+2)
 
        dp[idxp1] = (c*gamma1)/(gamma2*gamma3) 
    else:
        raise AssertionError("Wrong quadrature type!")

    if number_flag:
        return dp[0]
    else:
        return dp

#-- djacobi_p.py ---------------------------------------------------------------
