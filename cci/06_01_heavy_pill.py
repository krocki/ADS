# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-13 21:28:04
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-14 12:18:29

# 6.1
# You have 20 bottles of pills. 
# 19 bottles have 1 gram pill, but one has pill of weight 1.1 grams.
# Given a scale that provides an exact measurement, how would you find the heavy bottle?
# You can only use the scale once

# solution
# take 1 pill from bottle #1
# take 2 pills from bottle #2...
# take 20 pills from bottle #20

# if result -> 210.1 -> #1
# if result -> 210.2 -> #2
# ..
# if result -> 210.9 -> #9
# ..
# if result -> 220 -> #20
