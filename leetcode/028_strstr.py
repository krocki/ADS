# -*- coding: utf-8 -*-
# @Author: kamilrocki
# @Date:   2017-02-08 19:07:35
# @Last Modified by:   kamilrocki
# @Last Modified time: 2017-02-08 19:07:38

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l = len(needle)
        if haystack == needle: return 0
        
        for i,x in enumerate(haystack):
            w = haystack[i:i+l]
            if w == needle:
                return i
        
        return -1