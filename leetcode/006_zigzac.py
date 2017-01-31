# -*- coding: utf-8 -*-
# @Author: Kamil Rocki
# @Date:   2017-01-31 14:36:35
# @Last Modified by:   Kamil Rocki
# @Last Modified time: 2017-01-31 15:28:53

def convert(s, numRows):

	if not s: return ""

	lines = [''] * numRows
	print lines
	row = 0
	direction = 1

	for i in s:
		lines[row] += i
		if row <= 0:
			direction = 1
		if row == numRows-1:
			direction = -1
		
		row += direction
		

	return "".join(lines)
	

print convert("ABCD", 1)