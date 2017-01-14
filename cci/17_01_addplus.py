# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-13 19:51:00
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-13 21:21:41

# Write a function that adds two numbers. 
# You should not use + or any arithmetic operators

def myadd(M,N):

	if N == 0: return M

	#without carry
	O1 = M ^ N
	C = (M & N) << 1
	
	return myadd(O1,C)

N = 55
M = 44

O = myadd(M,N)

print O
