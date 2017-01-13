# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-13 12:21:30
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-13 13:26:40

def make_change(amount, available_coins):
	
	change = []

	if amount == 0: return [[]]
	if len(available_coins) == 0: return []

	x = available_coins[0]

	# 1. if x <= amount
	if x <= amount:

		#use 1st coin
		remaining = make_change(amount-x, available_coins)
		change = map (lambda y: [x]+y, remaining)
		
		change = change + make_change(amount, available_coins[1:])
	
	#x > amount
	else:

		#don't use 1st coin
		if len(available_coins) > 1:
			change = change + make_change(amount, available_coins[1:])
	
	return change

coins = [200,100,50,20,10,5,2,1]
print len(make_change(200, coins))
