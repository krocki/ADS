# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-13 19:49:40
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-13 20:01:35

# write a function to swap a number in place 
# (without a temporary variables)

x = 2
y = -5

print '%d %d' % (x, y)

x = x ^ y
y = x ^ y
x = x ^ y

print '%d %d' % (x, y)
