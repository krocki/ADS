# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-24 15:05:48
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-24 15:05:51

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
