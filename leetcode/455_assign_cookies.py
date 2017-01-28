# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-01-27 17:57:15
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-01-27 18:04:34

def findContentChildren(g, s):
	
	cnt = 0
	i = 0
	j = 0
	g.sort()
	s.sort()

	while i < len(g):
		if j >= len(s): break
		if g[i] <= s[j]:
			cnt += 1
			i += 1
		j += 1

	return cnt
	"""
	:type g: List[int]
	:type s: List[int]
	:rtype: int
	"""

print findContentChildren([1,2], [1,2,3])