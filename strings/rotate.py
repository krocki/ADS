# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-11 14:24:19
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-11 14:35:00

def array_left_rotation(a, n, k):
	
	return a[int(k):] + a[:int(k)]

n, k = raw_input().split()
arr = map(int, raw_input().split())

rotated = array_left_rotation(arr, n, k);

print rotated


