# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-02-05 22:51:12
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-02-05 22:51:14

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        
        p = math.log(n, 3)
            
        if 3**round(p) - n == 0:

            return True
        else:
            return False
        