
#-------------------------------------------------------------------------------
# Name:        Heat Exchanger Core creation
# Author:      rmaries@gmail.com
# Created:     31/12/2013
#!/usr/bin/env python


import ansa
import itertools
from ansa import base
from ansa import constants

def he_core():
	ents = ("CURVE", "FACE")
	results = base.PickNodes(constants.NASTRAN, ents)
	base.Not(base.CollectEntities(constants.NASTRAN,None,' __ALL_ENTITIES__'))
	nod_list = []
	curve_list = []
	cons_list=[]
	cons_set = []
	collector = base.CollectNewModelEntities()
	for ent in results:
		ret = base.GetEntityCardValues(constants.NASTRAN, ent, ("X1", "X2", "X3"))
		nod_list.append([ret['X1'], ret['X2'], ret['X3']])
	point_list = [[i[0],i[1],i[2]] for i in nod_list]
	trans = list(zip(*point_list))
	edge_point_list = list(itertools.product(trans[0], trans[1], trans[2]))
	for i in range(4):
		curve_points = [edge_point_list[i],edge_point_list[i+4]]
		trans_curve = list(zip(*curve_points))
		curve_list.append(base.CreateCurve(2,list(trans_curve[0]),list(trans_curve[1]),list(trans_curve[2])))
	for i in range(2):
        base.FacesNewFitted([curve_list[i],curve_list[i+1]])
        base.FacesNewFitted([curve_list[i],curve_list[i+2]])
    for i in collector.report():
        if i._ansaType == 'CURVES':
            base.Delete(i)
    base.Topo()
    base.Orient()
	base.All()
	base.Compress('')
		
if __name__ == '__main__':
	he_core()



