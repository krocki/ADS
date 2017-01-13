# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-12 21:20:19
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-12 21:35:33

def distance(a, b):

	a = sorted(a)
	print a

	b = sorted(b)
	print b

	if len(a) == 0: return len(b)
	if len(b) == 0: return len(b)

	if a[0] < b[0]:
		if len(a) > 0: return 1 + distance(a[1:], b)
		else: return len(b)

	if a[0] > b[0]:
		if len(b) > 0: return 1 + distance(a, b[1:])
		else: return len(a)

	if a[0] == b[0]:
		if len(a) > 0 and len(b) > 0: return distance(a[1:], b[1:])
		else: return 0

print distance("145", "5678")
