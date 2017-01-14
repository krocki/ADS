# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-13 19:39:38
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-14 11:37:07

# Write code to remove duplicates from an unsorted
# linked list
# How would you solve this problem if
# a temporary buffer is not allowed?

# 1. hash table, if collision -> is duplicate
# def remove_dups(x):

# 	size = 256
# 	lookuptable = [False] * size
# 	to_be_removed = []

# 	for (i,n) in enumerate(x):
# 		val = ord(n)
# 		if lookuptable[val]: 
# 			to_be_removed.append(i)
# 		else: lookuptable[val] = True

# 	for k in reversed(sorted(to_be_removed)):
# 		del x[k]

# 	return x

# 2. without temp buffer - O(n^2) time, double loop
def remove_dups(x):

	i = len(x)-1
	while i>=0:
		j = i-1
		while j>=0:
			if x[j] == x[i]:
				del x[j]
				i -= 1
			j -= 1
		i -= 1
	return x

print remove_dups(list("abvvcvvvvvccccc"))
