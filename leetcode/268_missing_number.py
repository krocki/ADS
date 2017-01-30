# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-29 19:46:19
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-29 19:46:21

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        expected = n * (n + 1)/2
        s = expected - sum(nums)

        return s
