# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-02-05 23:02:55
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-02-05 23:02:57
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        n = 0
        m = x
        
        while x != 0:
            d = x % 10
            print d
            x = x/10
            n = n*10 + d
            print n
        
        return m == n