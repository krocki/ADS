# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-13 19:38:27
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-13 20:06:13

# Implement an algorithm to determine if a string
# has all unique characters. What if you cannot
# use additional data structures?


def is_unique(string):

	s = sorted(string)

	if len(s) == 1: return True

	for i in range(1,len(s)):
		if s[i] == s[i-1]:
			return False

	return True

print is_unique("837451djfcyq")
