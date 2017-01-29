# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-28 20:50:48
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-28 20:58:21

def minCost(costs):

	"""
	:type costs: List[List[int]]
	:rtype: int
	"""
	if len(costs) == 0: return 0
	
	previous = 0, 0, 0

	for i,e in enumerate(costs):
		previous = costs[i][0] + min(previous[1], previous[2]), costs[i][1] + min(previous[0], previous[2]), costs[i][2] + min(previous[0], previous[1])

	return min(previous)
