# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-24 16:08:29
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-24 16:08:31

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        d = {}
        intersection = []
        
        for x in nums1:
            k = d.get(x)
            if k: d[x] += 1
            else: d[x] = 1
        
        for x in nums2:
            k = d.get(x)
            if k: 
                if (d[x] > 0): intersection.append(x)
                d[x] -= 1
        
        return intersection
