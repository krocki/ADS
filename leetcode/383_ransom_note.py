# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-28 20:34:39
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-28 20:39:57

def canConstruct(ransomNote, magazine):
	"""
	:type ransomNote: str
	:type magazine: str
	:rtype: bool
	"""
	d = {}

	for m in magazine:
		d[m]=d.get(m,0)+1

	for r in ransomNote:
		d[r]=d.get(r,0)-1
		if d[r] < 0:
			return False

	return True
