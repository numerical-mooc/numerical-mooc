# 
# 1D mesh generation
# ==================
# Generate simple equidistant grid with a given number of elements elements
#
# by Alberto Costa Nogueira Jr. (Matlab and Python versions)
#    Renato Cantao (Python version)
#
from simulation_data import SimulationData
import numpy as np

class Mesh1D:
    """Simple one-dimensional mesh.
    
    Arguments:
        sim_data - SimulationData object
    """
    def __init__(self, sim_data):
        # Generate node coordinates
        # - Note that we have n_elements+1 points on the domain.
        # - The name 'coord' is classic in FEM codes.
        self.coord = numpy.linspace( sim_data.spatial_domain[0],
                                  sim_data.spatial_domain[1],
                                  sim_data.n_elements+1 )

        # Element to node connectivity
        # - The name 'conn' is classic in FEM codes.
        self.conn = numpy.array([numpy.arange(0, sim_data.n_elements, 1),
                              numpy.arange(1, sim_data.n_elements+1, 1)]).T

    def jacobian(self, sim_data, quad_data):
        nip = sim_data.nip()

        # The Jacobian
        self.J = 0.5*(self.coord[1:]-self.coord[0:-1])

        # Elements' mid-points
        B = 0.5*(self.coord[1:]+self.coord[0:-1])
        # We repeat and reshape the array. Why?
        B = numpy.repeat(B, nip).reshape(sim_data.n_elements, nip).T

        # The transformed points. The construct 'numpy.newaxis' is needed here
        # because we want a de facto matricial product (rank-1 update).
        #
        # x = xi^T * J
        self.x = quad_data.xi[numpy.newaxis].T.dot(self.J[numpy.newaxis]) + B

#-- mesh_gen_1d.py -------------------------------------------------------------
