# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-22 20:33:50
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-22 21:08:01

# Given a list_of_ints, find the highest_product
# you can get from three of the integers. The
# input list_of_ints will always have at least
# three integers.

from operator import mul

def brute_force(a):

	best_prod = -9999

	for i in range(0, len(a)-2):
		for j in range(i+1, len(a)-1):
			for k in range(j+1, len(a)):
				prod = a[i] * a[j] * a[k]
				if prod > best_prod:
					best_prod = prod

	print best_prod

#does not work if there are negative numbers
def improved(a):

	three_highest = []
	best_prod = -9999

	for i in range(0, len(a)):
		
		three_highest.append(a[i])
		three_highest = sorted(three_highest)
		if len(three_highest) > 3: three_highest.pop(0)
		best_prod = max(best_prod, reduce(mul, three_highest, 1))

	print best_prod

def final(a):

	h = max(a[0],a[1])
	l = min(a[0],a[1])

	h2 = a[0] * a[1]
	l2 = a[0] * a[1]

	h3 = a[0] * a[1] * a[2]

	for i in range(2, len(a)):
		h3 = max(h3, a[i] * h2, a[i] * l2)
		h2 = max(h2, a[i] * h, a[i] * l)
		l2 = min(l2, a[i] * l, a[i] * h)
		l = min(a[i], l)
		h = max(a[i], h)

	print h3

a = [5, 2, 44, 12, 9, 2, 3, 4, 8, 9, 19, 32, 6, 50, 7, 11, 99, 1, 32, 42, 41, 6, 21, 31, 41, 95]
brute_force(a)
improved(a)
final(a)
