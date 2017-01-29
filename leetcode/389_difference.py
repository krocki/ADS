# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-01-27 11:26:04
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-01-27 17:07:21

def findTheDifference(s, t):
	"""
	:type s: str
	:type t: str
	:rtype: str
	"""
	d = {}

	for i in t:
		d[i] = d.get(i, 0) + 1

	for i in s:
		d[i] = d.get(i, 0) - 1

	for k,v in d.iteritems():
		if v > 0: return k

	return ""
	
print findTheDifference("abcd", "abcde")