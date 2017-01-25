# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-25 11:44:08
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-25 11:44:11

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

def sum_sublist(sublist, depth):
    
    sum = 0

    for i in sublist:
        if i.isInteger(): sum += i.getInteger() * depth
        else: sum += sum_sublist(i.getList(), depth+1)
    
    return sum
    
class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        
        return sum_sublist(nestedList, 1)
