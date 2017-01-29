# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-01-27 18:10:11
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-01-27 18:12:40

#same as decrementing one at a time
#for [1,2,3] -> 1. [1,2,2], 2. [1,1,2], 3. [1, 1, 1]

def minMoves(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	return sum(nums) - min(nums) * len(nums)
