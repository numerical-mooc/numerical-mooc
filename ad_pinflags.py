""" This program will check whether adhesive pinflags DOF is 123456, 
    if not DOF will set to 123456
"""
import ansa
from ansa import base
from ansa import constants

def ad_pinflags():
    adhes = base.CollectEntities(constants.NASTRAN, None, "AdhesiveLine_Type")
    for ent in adhes:
        dof = base.GetEntityCardValues(constants.NASTRAN, ent, ('RefC Pinflags',))
        print(dof['RefC Pinflags'])
        if dof['RefC Pinflags'] != 123456:
            print(ent._id, dof['RefC Pinflags'])
            base.SetEntityCardValues(constants.NASTRAN, ent, {'RefC Pinflags':123456})

ad_pinflags()
