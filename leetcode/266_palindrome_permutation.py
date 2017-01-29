# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-01-25 16:31:27
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-01-25 16:35:50

def canPermutePalindrome(s):

	"""
	:type s: str
	:rtype: bool
	"""
	nums = {}

	for i in s:
		nums[i] = nums.get(i, 0) + 1

	allowable_odd = len(s) % 2

	for k,v in nums.iteritems():
		if v % 2 == 1:
			allowable_odd -= 1
		if allowable_odd < 0:
			return False

	return True
	
print canPermutePalindrome("code")
print canPermutePalindrome("aab")
print canPermutePalindrome("carerac")
