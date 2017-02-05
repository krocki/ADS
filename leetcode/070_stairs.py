# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-02-04 21:18:49
# @Last Modified by:   krocki
# @Last Modified time: 2017-02-04 21:18:51

d = {}

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        global d
        
        ans = d.get(n)
        
        if ans: return ans
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n > 2:
            s_n1 = d.get(n-1, self.climbStairs(n-1))
            s_n2 = d.get(n-2, self.climbStairs(n-2))
            d[n-1] = s_n1
            d[n-2] = s_n2
            return s_n1 + s_n2
        
