# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-04 15:21:42
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-04 15:21:45

#!/bin/python

import sys


n = int(raw_input().strip())
counter = 0
maxcnt = 0

while (n):
    if (n & 1): counter=counter+1
    else: counter=0
    if counter > maxcnt: maxcnt = counter
    n >>= 1
    
print maxcnt