# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-23 21:10:26
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-23 21:10:37

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {}
        
        for i in range(0,len(s)):
            k = map.get(s[i])
            if k: map[s[i]] += 1
            else:  map[s[i]] = 1
        
        for i in range(0,len(s)):
            if map[s[i]] == 1:
                return i
                
        return -1
