# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-13 19:42:32
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-13 20:30:56

# you are given two 32-bit numbers, N and M, and
# two bit positions, i and j. Write a method to
# insert M into N such that M starts at bit j and
# ends at bit i. You can assume bits j through i
# have enough space to fit all of M. That is, if M
# = 10011, you can assume that there are at least
# 5 bits between j and i You would not, for
# example, have j = 3 and i = 2, because M could
# not fit between bit 3 and bit 2.

# EXAMPLE:
# input: N = 10000000000
#		 M = 10011, i = 2, j = 6
# output: 10001001100
#		  bit 65432xx

# N = 10000000000
# M = 00000010011
# i = 2 -> (M << 2) | N

N = 1024
M = 19

N = (M << 2) | N

print "{0:b}".format(N)
