# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-24 16:01:33
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-24 16:01:35

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
    
        for x in nums:
            k = d.get(x)
            if k: return True
            d[x] = 1

        return False
