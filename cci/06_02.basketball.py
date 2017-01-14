# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-14 12:25:57
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-14 12:38:52

# you have a basketball hoop and someone says that you can play one of two games
# game 1: you get one shot to make the hoop
# game 2: you get three shots and you have to make 2 of 3
# if p is the probability of making a particular shot, for which values of p
# should you pick one game or the other

# case 1: P = p
# case 2: P = 3*p^2(1-p) + p^3  = -2p^3 + 3p^2 (binomial (3 k) where k>=2

# -2p^2 + 3p - 1 > 0
# 2p^2 - 3p + 1 < 0
# (2p - 1)(p - 1) < 0
# (p - 1) < 0, so (2p - 1) > 0, 2p > 1, p > 1/2
# P is higher for game #2 if p > 1/2
