# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-01-25 17:18:22
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-01-25 17:54:45

cache = {}
calls = 0

def canWinNim(n):
	"""
	:type n: int
	:rtype: bool
	"""
	global calls
	global cache

	calls += 1

	if n == 0: 
		cache[0] = False 
	if 0 < n < 4:
		cache[n] = True 
	else:
		k = cache.get(n)
		if not k: cache[n] = not cache.get(n-1, canWinNim(n-1)) or not cache.get(n-2, canWinNim(n-2)) or not cache.get(n-3, canWinNim(n-3))

	return cache[n]

print [(x,canWinNim(x)) for x in range(5,33)]
print calls