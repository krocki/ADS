# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-01-27 17:08:32
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-01-27 17:21:06

# https://en.wikipedia.org/wiki/Digital_root#Congruence_formula

def addDigits(num):
    
	if num == 0: return 0
	else: return 1 + (num - 1) % 9

	"""
	:type num: int
	:rtype: int
	"""
