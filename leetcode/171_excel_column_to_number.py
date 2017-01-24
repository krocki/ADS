# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-23 21:22:32
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-23 21:26:13

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        c_idx = 0
        
        for i in range(len(s)-1, -1, -1):
            letter_val = ord(s[i]) - 64
           
            c_idx += letter_val*26**(len(s)-i-1)
        
        return c_idx
        
