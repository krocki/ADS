# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-22 15:50:46
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-22 16:07:08

# Given a list of day stock prices (integers for
# simplicity), find the maximum single sell
# profit.

# We need to maximize the single buy/sell profit and
# in case we can't make any profit, we'll try to
# minimize the loss. For below examples, buy and
# sell prices for making maximum profit are
# highlighted. 

def max_profit(d):

	b = buy = d[0];
	s = sell = d[1];
	best_profit = sell - buy

	for i in range(1, len(d)):
		current_profit = d[i] - buy
		
		if current_profit > best_profit:
			best_profit = current_profit
			sell = d[i]
			b = buy
			s = sell

		if d[i] < buy:
			buy = d[i]

	return b, s, best_profit


x = [21, 12, 11, 9, 6, 3]
y = [8, 5, 12, 9, 19, 1]

print max_profit(x)
print max_profit(y)
