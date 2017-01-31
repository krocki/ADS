# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-30 20:39:54
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-30 20:42:58

def countBits(num):
	"""
	:type num: int
	:rtype: List[int]
	"""
	ret = [0] * (num + 1)

	for i in range(1, num+1):
	    ret[i] = 1 + ret[i & (i - 1)]
	    
	return ret

print countBits(2)
