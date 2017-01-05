# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-04 14:21:30
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-04 14:34:11

cases = input()

for k in range (0, cases):

	str = raw_input()
	a = ""
	b = ""
	for i in range(0, len (str)):
		if i % 2 == 0: a += str[i]
		else : b += str[i]
	print a + " " + b