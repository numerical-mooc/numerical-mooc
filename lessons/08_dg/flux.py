# 
# Numerical flux
# ==============
#
# by Alberto Costa Nogueira Jr. (Matlab and Python versions)
#    Renato Cantao (Python version)
#
from simulation_data import BasisType
import numpy

class Fluxes:
    def __init__(self, sim_data):
        nldof = sim_data.n_local_dof()

        if sim_data.basis_type == BasisType.MODAL_ORTHOGONAL:
            self.FR = numpy.ones([nldof, nldof])
            # Ok, couldn't resist it :-D
            self.FL = numpy.array([[(-1.0)**i * (-1.0)**j for i in xrange(nldof)]
                for j in xrange(nldof)])
            self.FRp1 = numpy.array([[(-1.0)**i for i in xrange(nldof)]
                for j in xrange(nldof)])
            self.FLm1 = numpy.array([[(-1.0)**j for i in xrange(nldof)]
                for j in xrange(nldof)])
        else:
            self.FR = numpy.zeros([nldof, nldof])
            self.FL = numpy.zeros([nldof, nldof])
            self.FRp1 = numpy.zeros([nldof, nldof])
            self.FLm1 = numpy.zeros([nldof, nldof])

            self.FR[-1, -1] = 1.0
            self.FL[0, 0] = 1.0
            self.FRp1[-1, 0] = 1.0
            self.FLm1[0, -1] = 1.0

#-- flux.py --------------------------------------------------------------------
