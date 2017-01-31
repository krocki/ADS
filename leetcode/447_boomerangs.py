# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-30 15:21:21
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-31 08:06:09

# Input:
# [[0,0],[1,0],[2,0]]

# Output:
# 2

# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

def boomerangs(points):

	result = 0

	for a in points:
		d1 = {}
		for b in points:
			dist = (a[0] - b[0])**2 + (a[1] - b[1])**2
			d1[dist] = d1.get(dist,0) + 1
			result += 2*(d1[dist]-1)

	return result

print boomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]])

