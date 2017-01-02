# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-01 18:15:53
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-01 18:15:59

#!/bin/python

import sys

N = int(raw_input().strip())

if N % 2 == 1:
    print "Weird"
else:
    if N <= 5:
        print "Not Weird"
    elif N <= 20:
        print "Weird"
    else:
        print "Not Weird"
