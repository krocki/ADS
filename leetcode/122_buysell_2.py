# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-29 19:43:32
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-29 19:43:35

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        
        for i in range(1, len(prices)):
            p = prices[i] - prices[i-1]
            if p > 0:
                total += p
        
        return total
