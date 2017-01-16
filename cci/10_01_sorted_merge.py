# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-13 19:47:53
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-13 22:11:01

# You are given two sorted arrays, A and B, where
# A has a large enough buffer at the end to hold
# B. Write a method to merge B into A in sorted
# order.

A = [4,4,1,7,2,3442,234,541,-234]
B = [-23,5,7,8,1,2,3]

# TODO: insert into A without extra space
#		merge backwards into the end of A

def merge(a,b):

	merged = []

	a0 = a[0]
	b0 = b[0]

	if b0 <= a0:
		merged += [b0]
		if len(b) == 1: merged += a
		if len(b) > 1: merged += merge(a, b[1:])
	else:
		merged += [a0]
		if len(a) == 1: merged += b
		if len(a) > 1: merged += merge(a[1:], b)

	return merged

x = sorted(A)
y = sorted(B)
print "Before merge"
print "A"
print x
print "B"
print y
z = merge(x,y)
print "merged(A,B)"
print z
