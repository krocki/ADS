# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-30 21:07:43
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-30 21:11:04

def wiggleSort(nums):

	for i in range(1, len(nums)):
		if i % 2 == 0:
			if nums[i] > nums[i-1]:
				tmp = nums[i]
				nums[i] = nums[i-1]
				nums[i-1] = tmp
		else:
			if nums[i] < nums[i-1]:
				tmp = nums[i]
				nums[i] = nums[i-1]
				nums[i-1] = tmp	
	
	print nums

print wiggleSort([3, 5, 2, 1, 6, 4])
