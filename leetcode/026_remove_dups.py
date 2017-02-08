# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-02-07 20:23:49
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-02-07 20:23:51

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] == nums[i]:
                nums.pop(i)
            
        return len(nums)