# -*- coding: utf-8 -*-
# @Author: kmrocki@us.ibm.com
# @Date:   2017-02-12 20:30:00
# @Last Modified by:   kmrocki@us.ibm.com
# @Last Modified time: 2017-02-12 20:30:02

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        else: return n & (n-1) == 0