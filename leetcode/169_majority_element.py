# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-24 15:29:38
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-24 15:29:48

class Solution(object):
    def majorityElement(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """
        
        d = {}
        l = len(nums)
        
        for n in nums:
            
            k = d.get(n)
            if k: d[n] += 1
            else: d[n] = 1
            
        for key, value in d.iteritems():
            if value > l/2:
                return key
        
        return 0
        
