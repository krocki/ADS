# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-13 19:46:14
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-13 20:47:07

# A child is running up a staircase with n
# stepsand can hop either 1 step, 2 steps, or 3
# steps at a time Implement a method to count how
# many possible ways the child can run up the
# stairs

def ways(n, possible_steps):

	combinations = []
	l = len(possible_steps)

	if n == 0: return [[]]
	if l == 0: return []

	x = possible_steps[0]

	if n >= x:
		#1. take step x
		combinations = [[x] + y for y in ways(n-x, possible_steps)]
		#2. choose not to take x
		if l > 1: combinations += ways(n, possible_steps[1:])
	
	else:
		# step x not possible
		if l > 1: combinations += ways(n, possible_steps[1:])

	return combinations

n = 15
combinations = ways(n, [3,2,1])
print combinations
print len(combinations)

