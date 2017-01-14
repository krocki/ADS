# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-14 14:25:27
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-14 14:35:22

# given 2 strings. write a method to decide if one is a permutation of the other

# BCR = O(N)

# 1. sort a and b, go through them and compare all elements. Total O(NlogN)
# 2. use a table to count # of characters in b - N time, go through a and do the same thing but subtract, N time

# 1
# def is_permutation(a, b):

# 	if len(a) != len(b):
# 		return False

# 	a0 = sorted(a)
# 	b0 = sorted(b)

# 	for i,n in enumerate(a0):
# 		if a0[i] != b0[i]:
# 			return False

# 	return True

# 2

def is_permutation(a, b):

	if len(a) != len(b):
		return False

	lookup_table = [0] * 256

	for i,n in enumerate(b):
		lookup_table[ord(b[i])] += 1

	for i,n in enumerate(a):
		lookup_table[ord(a[i])] -= 1

	for i,n in enumerate(lookup_table):
		if lookup_table[i] != 0:
			return False

	return True

print is_permutation(list("abc"), list("cba"))
print is_permutation(list("abc"), list("cb"))
print is_permutation(list("abc"), list("cbc"))
