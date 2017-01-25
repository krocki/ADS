# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-25 11:16:43
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-25 11:16:49

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        mask = -1
    
        while num & mask:
             mask <<= 1
    
        return ~mask & ~num
        
