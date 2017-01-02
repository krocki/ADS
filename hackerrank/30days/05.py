# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-01 18:31:11
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-01 18:31:15

#!/bin/python

import sys

n = int(raw_input().strip())

for i in range(1, 11):
    print str(n) + " x " + str(i) + " = " + str(i * n)
