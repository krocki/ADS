# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-22 15:50:46
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-22 19:15:46

# Given a list of day stock prices (integers for
# simplicity), find the maximum single sell
# profit.

# We need to maximize the single buy/sell profit and
# in case we can't make any profit, we'll try to
# minimize the loss. For below examples, buy and
# sell prices for making maximum profit are
# highlighted. 

def max_profit(d):

	if len(d) < 2:
	    raise IndexError('len < 2')

	best_profit = d[1] - d[0]
	buy = d[0]

	for i, price in enumerate(d):
		if i == 0:
		    continue

		current_profit = price - buy
		best_profit = max(current_profit, best_profit)
		buy = min(buy, price)

	return best_profit


x = [21, 12, 11, 9, 6, 3]
y = [8, 5, 12, 9, 19, 1]

print max_profit(x)
print max_profit(y)

