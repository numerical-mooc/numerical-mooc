#
# Common simulation data
# ======================
# It presents a struct to store simulation data common to all problemas, like
# number of elements, polynomial order and so on.
#
# by Alberto Costa Nogueira Jr. (Matlab and Python versions)
#    Renato Cantao (Python version)
#
from math import ceil, floor

#
# Used to specify the chosen basis.
#
class BasisType(object):
    """The available basis types."""
    NODAL = 0
    MODAL = 1
    MODAL_ORTHOGONAL = 2
    MODAL_ORTHONORMAL = 3

#
# Used to specify the chosen type of points distribution for Gaussian quadrature
#
class QuadratureNodes(object):
    """The available quadrature nodes distribution."""
    GL  = 0     # Gauss-Legendre
    GLL = 1     # Gauss-Legendre-Lobatto

class SimulationData:
    """Creates a simulation data structure."""
    def __init__(self,
                 n_elements      = 1,
                 poly_order      = 0,
                 spatial_domain  = (0.0, 1.0),
                 temporal_domain = (0.0, 1.0),
                 basis_type      = BasisType.NODAL,
                 node_dist       = QuadratureNodes.GL,
                 non_linear      = False):
        """
        Parameters
        ----------
        n_elements
            Number of elements
        poly_order
            Polynomial order of approximation
        spatial_domain
            Spatial domain
        temporal_domain
            Temporal domain
        basis_type
            The basis used in the approximation
        node_dist
            The quadrature points distribution
        """
        self.n_elements      = n_elements
        self.poly_order      = poly_order
        self.spatial_domain  = spatial_domain
        self.temporal_domain = temporal_domain
        self.basis_type      = basis_type
        self.node_dist       = node_dist
        self.non_linear      = non_linear

    def mass_order(self):
        """Number of integration points needed for mass matrix assembly."""
        return self.poly_order*2

    def nonlinear_order(self):
        """Number of integration points needed for nonlinear terms."""
        return self.poly_order*3

    def spatial_domain_length(self):
        """Length of the spatial domain."""
        return self.spatial_domain[1] - self.spatial_domain[0]

    def n_local_dof(self):
        """Local degrees of freedom.
        
        In 1D we have the polynomial order plus 1, to account for the constant
        term."""
        return self.poly_order+1

    def n_global_dof(self):
        """Global degrees of freedom."""
        return self.n_local_dof()*self.n_elements

    def nip(self):
        order = self.mass_order() if self.non_linear == False else self.nonlinear_order()

        if self.node_dist == QuadratureNodes.GL:
            return int(ceil(0.5*(order+2)))
        elif self.node_dist == QuadratureNodes.GLL:
            # floor(nip) will keep the nodal spectral approach Np = N+1
            return int(floor((order+3)/2))
        else:
            raise AssertionError( "Wrong quadrature node distribution!\n" )

    def t_min(self):
        return self.temporal_domain[0]

    def t_max(self):
        return self.temporal_domain[1]

    # Boilerplate code
    def __str__(self):
        return ("SimulationData:\n"
                "  Number of elements: %s\n"
                "  Polynomial order  : %s\n"
                "  Spatial domain    : %s\n"
                "  Temporal domain   : %s") % (self.n_elements,
                                               self.poly_order,
                                               self.spatial_domain,
                                               self.temporal_domain)

#-- simulation_data.py ---------------------------------------------------------
