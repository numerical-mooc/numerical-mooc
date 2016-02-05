#
# Jacobi polynomials evaluated at a point or vector
#
# by Alberto Costa Nogueira Jr. (Matlab and Python versions)
#    Renato Cantao (Python version)
#
from numbers import Number
import numpy

def jacobi_p(x, m, alpha = 0.0, beta = 0.0):
    """Jacobi polynomial."""
    number_flag = False

    if isinstance(x, Number):
        x = numpy.array([x])
        number_flag = True

    aPb = alpha+beta   # mnemonics: alpha plus beta
    aMb = alpha-beta   # mnemonics: alpha minus beta

    Pn  = numpy.ones(x.shape)
    Pn1 = 0.5*(aMb+(aPb+2.0)*x)

    if m == 0:
        Pm = Pn
    elif m == 1:
        Pm = Pn1
    else:
        for n in range(1, m+1):
            n1 = n+1.0
            n2 = 2.0*n

            a1n = 2.0*n1*( n1+aPb )*( n2+aPb )
            a2n = ( n2+aPb+1.0 )*aPb*aMb
            a3n = ( n2+aPb )*( n2+aPb+1.0 )*( n2+aPb+2.0 )
            a4n = 2.0*( n+alpha )*( n+beta )*( n2+aPb+2.0 )

            Pn2 = ( ( a2n+a3n*x )*Pn1-a4n*Pn )/a1n
            Pn  = Pn1
            Pn1 = Pn2

        Pm = Pn

    if number_flag:
        return Pm[0]
    else:
        return Pm
 
#-- jacobi_p.py ----------------------------------------------------------------
