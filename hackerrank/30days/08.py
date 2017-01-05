# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-04 15:07:26
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-04 15:09:58

cases = input()

dict = {}

for k in range(0, cases):
    str = raw_input()
    entries = str.split()
    dict[entries[0]] = entries[1]

a = True

while (a):
    a = raw_input()
    number = dict.get(a)
    if number == None: print "Not found"
    else: print a + "=" + number