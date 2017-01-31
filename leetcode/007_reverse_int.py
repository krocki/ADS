# -*- coding: utf-8 -*-
# @Author: Kamil Rocki
# @Date:   2017-01-31 15:39:44
# @Last Modified by:   Kamil Rocki
# @Last Modified time: 2017-01-31 15:39:46

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0

        if x < 0: 
            s = -1
            x = -x
        else: s = 1
        
        while (x != 0):
            print x, res, x % 10
            res = res * 10
            res += x % 10
            x = x/10
           
        if (res > 1 << 31): return 0
        
        return res * s
        