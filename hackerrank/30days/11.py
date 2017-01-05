# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-04 15:35:10
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-04 15:35:13

#!/bin/python

import sys
¥
arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)
    
maxsum = None
for i in range(0,4):
    for j in range(0,4):
        sum = arr[j][i] + arr[j][i+1] + arr[j][i+2] + arr[j+1][i+1] + arr[j+2][i] + arr[j+2][i+1] + arr[j+2][i+2]
        if sum > maxsum: maxsum = sum
            
print maxsum