# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-24 17:03:21
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-24 19:33:08

# Input: n = 1 
# Return: ["1:00", "2:00", "4:00",
# "8:00", "0:01", "0:02", "0:04", "0:08", "0:16",
# "0:32"]

def bin_to_time(bitstring):

	h = bitstring[0] * 8 + bitstring[1] * 4 + bitstring[2] * 2 + bitstring[3] * 1
	m = bitstring[4] * 32 + bitstring[5] * 16 + bitstring[6] * 8 + bitstring[7] * 4 + bitstring[8] * 2 + bitstring[9] * 1

	if h < 12 and m < 60:
		return "%d:%02d" % (h,m)

def bin_string(n, l):

		bitstrings = []

		if l == 0: return [[]]

		elif n == l:
			bitstrings = [[1] + i for i in bin_string(n-1,l-1)]
			
		elif n == 0:
			bitstrings = [[0] + i for i in bin_string(n,l-1)]

		elif n < l:
			bitstrings = [[0] + i for i in bin_string(n,l-1)] + [[1] + i for i in bin_string(n-1,l-1)]

		return bitstrings
    		

def readBinaryWatch(num):

    """
    :type num: int
    :rtype: List[str]
    """

    t = [bin_to_time(i) for i in bin_string(num, 10)]

    return [i for i in t if i != None]

print readBinaryWatch(2)
