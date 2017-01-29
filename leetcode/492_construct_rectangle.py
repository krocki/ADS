# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-01-25 19:59:59
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-01-25 20:07:12

import math

def largest_factor(n):

	for i in range(int(math.sqrt(n)), 0, -1):
		if n % i == 0:
			return (n/i, i)

	return [n, 1]
	
class Solution(object):
	def constructRectangle(self, area):
		"""
		:type area: int
		:rtype: List[int]
		"""
		return largest_factor(area)