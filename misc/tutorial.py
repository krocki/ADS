# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-12 22:07:06
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-12 22:10:11

# list comprehension in python

def f(i,s):
	return '%d - %s' % (i, s)

s = ['a', 'b', 'c']

print [f(i,s) for i,s in enumerate(s)]
