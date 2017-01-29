# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-01-25 18:08:05
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-01-25 18:22:55

def findDisappearedNumbers(nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	missing = []

	for i,x in enumerate(nums):
		idx = abs(x)
		nums[idx-1] = abs(nums[idx-1]) * (-1)

	for i,x in enumerate(nums):
		if x > 0: missing.append(i+1)

	return missing

print findDisappearedNumbers([4,3,2,7,8,2,3,1])