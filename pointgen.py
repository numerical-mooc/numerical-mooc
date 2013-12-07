import itertools
def pointgen(x):
    '''
    x ---> list of coordinates of diagonal points of the box
    This function will create the coordinates for the edges of the box
    I assume that box is aligned with xyz plane
    '''
    trans = list(zip(*x))
    return list(itertools.product(trans[0],trans[1],trans[2]))
