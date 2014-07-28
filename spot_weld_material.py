""" This script is used to set the Material Density to 1e-16 whose PSHELL 
    name contains the string 'SPOT' in it
"""
import ansa
from ansa import base
from ansa import constants

def spot_weld_material():
    pid = base.CollectEntities(constants.NASTRAN, None, "__PROPERTIES__")
    for ent in pid:
        ret = base.GetEntityCardValues(constants.NASTRAN, ent, ('MID1',))
        if "SPOT" in ent._name:
            mat = base.GetEntity(constants.NASTRAN, "__MATERIALS__", ret['MID1'])
            rho = base.GetEntityCardValues(constants.NASTRAN, mat, ('RHO',))
            print(ent._id, ent._name, mat._id, mat._name, rho['RHO'])
            base.SetEntityCardValues(constants.NASTRAN, mat, {'RHO':1e-16})

spot_weld_material()
