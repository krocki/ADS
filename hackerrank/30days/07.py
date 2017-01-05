# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-04 14:52:05
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-04 14:52:07

#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

for k in range(len (arr)-1, -1, -1):
    print arr[k],