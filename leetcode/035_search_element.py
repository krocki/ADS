# -*- coding: utf-8 -*-
# @Author: kamilrocki
# @Date:   2017-02-08 19:16:33
# @Last Modified by:   kamilrocki
# @Last Modified time: 2017-02-08 19:16:35

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        
        if length == 1:
            if nums[0] >= target:
                return 0
            else:
                return 1
        
        m = nums[length/2]
        
        if target < m:
            return self.searchInsert(nums[:length/2], target)
        else:
            return length/2 + self.searchInsert(nums[length/2:], target)