"""
This is the script written in ANSA API 
1.To check all MID1, MID2, and MID3 should be same.(if not set it equal)
2.For PSHELL contains the 'Skin_' only MID 1 should be assigned with thickness assign 0.001. 
if not apply the thickness.
3.Should check MID4 should be blank."""

import ansa
from ansa import base
from ansa import constants
def check_mid():
    pid = base.CollectEntities(constants.NASTRAN, None, "PSHELL")
    mid = ('MID1','MID2','MID3')
    for ent in pid:
        mids = base.GetEntityCardValues(constants.NASTRAN, ent, mid)
        base.SetEntityCardValues(constants.NASTRAN, ent, {'MID4':""})
        if mids['MID1'] != mids['MID2'] or mids['MID1'] != mids['MID3']:
            print(ent._id, ent._name, mids['MID1'], mids['MID2'],mids['MID3'])
            base.SetEntityCardValues(constants.NASTRAN, ent, {'MID2':mids['MID1'], 'MID3':mids['MID1']})
    for tetskin in pid:
        if 'Skin_' in tetskin._name:
            base.SetEntityCardValues(constants.NASTRAN, tetskin, {'MID2':"", 'MID3':"", 'T':0.001})

check_mid()