# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-02-07 20:33:26
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-02-07 20:33:28

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
            
        return len(nums)