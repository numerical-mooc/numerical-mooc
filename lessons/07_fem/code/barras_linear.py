## Translation of mlb's barras_linear.m to Python
## cacs@thorus-scisoft.com.br

import numpy as np

## Physical data
Lb=1.0        # bar length
E  = 210e9       # Young modulus
A  = 1e-4        # cross sectional area
EA = E*A 
p0 = 100         # distributed load
Pc = 200         # concentrated load at x = L, b.c. at x = L

## FEM setup: all element with the same length
Nel   = 4        # number of elements       
Nvert = Nel+1    # number of nodes (1-D, linear interpolation)
he    = Lb/Nel   # element lenght
Ndofs = Nel+1    # number of d.o.f. (1 d.o.f. per node)

# Allocation of the stifness matrix
Kg = np.zeros((Ndofs,Ndofs))

# Allocation of the load vector
Fg = np.zeros(Ndofs)

# Allocation of the solution vector
ug = np.zeros(Ndofs)

# Allocation of incidence matrix
Incid = np.zeros((Nel,2), dtype=np.int)

# Auxiliary matrix for accessing submatrix (more comments below)
TIncid = np.zeros((2,1), dtype=np.int)

# Nodes coordinates
X = np.linspace(0, Lb, Nvert)

# Bar element stiffness matrix
Ke = (EA/he)*np.array([[1,-1],[-1,1]])

# Bar element load vector due to the distributed load p0
Fe = (p0*he/2)*np.array([1, 1])

# Assembly of global matrix and global load vector without b.c.'s
for e in range(0,Nel):
	Incid[e,:]=np.array([e,e+1])
	Fg[Incid[e,:]]=Fg[Incid[e,:]]+Fe 
	# numpy requires a column matrix to specify submatrix columns
	TIncid[:,0]=Incid[e,:] 
	# The general mechanism to access submatrices in numpy returns the
    # transpost of the submatrix. Despite all matrices being symmetric
	# I am transposing Ke to be coherent.
	Kg[Incid[e,:], TIncid] = Kg[Incid[e,:], TIncid] + np.transpose(Ke);

# Application of force b.c. at x = L
Fg[-1] = Fg[-1] + Pc

# Application of b.c. disp. condition at x = 0 (elimination of the first line
# and first column of the global system) and linear system solution
ug[1:] = np.linalg.solve( Kg[1:,1:],Fg[1:] )
