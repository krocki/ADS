# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-02-06 16:41:22
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-02-06 16:41:25

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        
        if len(strs) > 0:
            
            last = strs[-1]
            first = strs[0]
            
            if last == first: return last

            k = 0
            for k in range(0,len(first)):
                if first[k] != last[k]:
                    return first[:k]
            
            return first[:k+1]
        
        return ""
            