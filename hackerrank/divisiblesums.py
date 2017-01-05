# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-04 15:46:13
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-04 15:46:25

#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))
counter = 0

for i in range(0, n):
    for j in range(i+1, n):
        s = a[i] + a[j]
        if s % k == 0: counter = counter+1

print counter