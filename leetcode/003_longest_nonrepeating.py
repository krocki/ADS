# -*- coding: utf-8 -*-
# @Author: Kamil Rocki
# @Date:   2017-01-31 16:29:30
# @Last Modified by:   Kamil Rocki
# @Last Modified time: 2017-01-31 16:29:32

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        longest = 0
        last_unique = -1
        
        for i,x in enumerate(s):
            last_unique = max(last_unique, d.get(x, -1))
            current_seq = i - last_unique
            longest = max(longest, current_seq)
            d[x] = i
            
        return longest