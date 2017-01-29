# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-01-27 17:47:53
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-01-27 17:52:31

def moveZeroes(nums):
	"""
	:type nums: List[int]
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	i = 0
	k = 0
	while k < len(nums):
		if nums[k] == 0: 
			k += 1
		else:
			nums[i] = nums[k]
			i += 1
			k += 1
	nums[i:] = [0]*(k-i)

	print nums

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)