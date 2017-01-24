# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-23 21:37:59
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-23 21:43:14

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map = {}

        for x in s:
            k = map.get(x)
            if k:
                map[x] += 1
            else:
                map[x] = 1
        
        for x in t:
            k = map.get(x)
            if k:
                map[x] -= 1
            else:
                map[x] = -1 
                
        for key, value in map.iteritems():
            print key, value
            if value != 0:
                return False
                
        return True
