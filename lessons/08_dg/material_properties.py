#
# Sets several material properties for the elastic wave equation
#
# by Alberto Costa Nogueira Jr. (Matlab and Python versions)
#    Renato Cantao (Python version)
#
import numpy
from simulation_data import QuadratureNodes
from math import ceil

class MaterialProperties:
    """Material properties for the elastic wave equation"""
    def __init__(self, sim_data, quad_data, mesh, x_source):
        """MaterialProperties constructor

        Arguments:
            sim_data - SimulationData object
            quad_data - Quadrature points and weights
            mesh - 1D Finite Elements mesh
            x_source - Ricker wavelet point source location
        """
        nip   = sim_data.nip()
        nldof = sim_data.n_local_dof()
        dx    = sim_data.spatial_domain_length()

        self.rho   = numpy.zeros(sim_data.n_elements)         # Material density [kg/m^3]
        self.mu    = numpy.zeros([nip, sim_data.n_elements])  # Material shear modulus [Pa]
        self.c     = numpy.zeros([nip, sim_data.n_elements])  # Material wavefield velocity [m/s]
        self.dmudx = numpy.zeros([nip, sim_data.n_elements])  # Derivative of shear modulus

        # mu evaluated at the boundaries of each element including ghosts
        self.mub = numpy.zeros([nldof, sim_data.n_elements+2]) 
    
        # We could have set that above, but here is clearer
        self.rho.fill(1000.0)

        distance = 0.5*dx-mesh.x

        # Signal changes
        sg = numpy.sign(distance)

        distance = numpy.exp(-(numpy.fabs(distance)-500.0)/100.0)

        self.mu    = 1.2e10-5.96e9/(1.0+distance)
        self.dmudx = 5.96E9*(distance*sg)/(100.0*(1.0+distance)**2)
        self.c     = numpy.sqrt(self.mu/numpy.reshape(numpy.repeat(self.rho, nip), (nip, sim_data.n_elements)))

        distance1 = numpy.fabs(mesh.coord[0:-1]-0.5*dx)
        distance2 = numpy.fabs(mesh.coord[1:]-0.5*dx)

        self.mub[ 0, 1:-1] = 1.2e10-5.96e9/(1.0+numpy.exp(-(distance1-500.0)/100.0))
        self.mub[-1, 1:-1] = 1.2e10-5.96e9/(1.0+numpy.exp(-(distance2-500.0)/100.0))

        self.mub[-1,  0] = self.mub[0, 1]
        self.mub[ 0, -1] = self.mub[-1, -2]

        d = numpy.fabs(mesh.x.T.flatten()-x_source)
        dist = numpy.amin(d)         # The mininum
        globnode = numpy.argmin(d)   # The index
        self.el = int(ceil(globnode/nldof))
        self.locid = globnode-nldof*self.el

        if sim_data.node_dist == QuadratureNodes.GLL:
            if self.locid == 0:
                self.globid = globnode+1
                self.locid = self.locid+1
            elif locid == nldof-1:
                self.globid = globnode-1
                self.locid = self.locid-1
            else:
                self.globid = globnode
        elif sim_data.node_dist == QuadratureNodes.GL:
            self.globid = globnode

#-- material_properties.py -----------------------------------------------------
