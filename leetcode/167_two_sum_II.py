# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-01-27 17:38:42
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-01-27 17:45:46

def twoSum(numbers, target):

	i = 0
	j = len(numbers) - 1

	while (i < j):
		n = numbers[i] + numbers[j]
		if (n > target): j = j-1
		elif (n < target): i = i+1
		else: break

	return [i+1,j+1]
	"""
	:type numbers: List[int]
	:type target: int
	:rtype: List[int]
	"""

print twoSum([1,2,7,11,15], 9)