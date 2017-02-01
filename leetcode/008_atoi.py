# -*- coding: utf-8 -*-
# @Author: Kamil Rocki
# @Date:   2017-01-31 15:44:39
# @Last Modified by:   Kamil Rocki
# @Last Modified time: 2017-01-31 16:12:02

def myatoi(s):

	n = 0
	i = 0

	while s[i] is ' ':
		i += 1

	if s[i] is '-': 
		sgn = -1
		i += 1
	if s[i] is '+': 
		sgn = 1
		i += 1
	else: sgn = 1

	num = []

	while i < len(s) and s[i] <= '9' and s[i] >= '1':

		print s[i]
		num += s[i]
		i += 1

	d = 1
	for i in reversed(num):
		n += int(i)*d
		d *= 10
	return n * sgn

print myatoi("+1")