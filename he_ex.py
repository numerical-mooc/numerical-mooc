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
	intersection = 1	
	while intersection:		
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
		for i in range(0,8,2):
			curve_points = [edge_point_list[i],edge_point_list[i+1]]
			trans_curve = list(zip(*curve_points))
			curve_list.append(base.CreateCurve(2,list(trans_curve[0]),list(trans_curve[1]),list(trans_curve[2])))
		for i in range(2):
			base.FacesNewFitted([curve_list[i],curve_list[i+2]])
		for i in collector.report():
			if base.GetEntityType(constants.NASTRAN, i) == 'CONS':
				cons_list.append(i)
		for con in cons_list:
			cons_set .append( base.GetEntityCardValues(constants.NASTRAN, con, ('ID','Length')))
			length_list = [length['Length'] for length in cons_set]
		new_cons_list = list(cons_set)
		min_length  = round(min(length_list),4)		
		for new_lis in cons_set:			
			if round(new_lis['Length'],4) != min_length:
				new_cons_list.remove(new_lis)		
		req_cons_list = [base.GetEntity(constants.NASTRAN, "CONS", cons['ID']) for cons in new_cons_list]		
		for c in range(2):
			base.FacesNewFitted([req_cons_list[c],req_cons_list[c+2]])
		base.Orient()
		if base.CheckIntersections(True,True):
			base.DeleteEntity(collector.report(), True)
		else:
			intersection = 0
	base.All()
	base.Compress('')
		
if __name__ == '__main__':
	he_core()



