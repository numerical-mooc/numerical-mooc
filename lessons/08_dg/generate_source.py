#
# Sets several material properties for the elastic wave equation
#
# by Alberto Costa Nogueira Jr. (Matlab and Python versions)
#    Renato Cantao (Python version)
#
import numpy
from math import floor

def generate_source(sim_data, mesh, mat_prop):
    v_max = numpy.amax(mat_prop.c)
    Delta_x_min = numpy.amin(numpy.fabs(mesh.x[0, :]-mesh.x[1, :]))
    CFL = 0.4
    
    dt = CFL*Delta_x_min/v_max
    Nsteps = int(floor(sim_data.t_max()/dt))
    dt = sim_data.t_max()/float(Nsteps)
    
    t_source = 0.1*sim_data.t_max()
    sigma = t_source
    
    # Ricker wavelet over the domain [-5,+5]
    t_eval = numpy.linspace(-5.0, 5.0, floor(t_source/dt))
    Ricker_wavelet = numpy.zeros(Nsteps)
    Ricker_wavelet[0:t_eval.shape[0]] = (2.0/(numpy.sqrt(3.0*sigma)*numpy.pi**0.25))*\
            (1.0-(t_eval/sigma)**2)*numpy.exp(-0.5*(t_eval/sigma)**2)
    
    # Note: the 6e7 is an arbitrary reescaling
    return 6e7*Ricker_wavelet, dt, Nsteps

#-- generate_source.py ---------------------------------------------------------
