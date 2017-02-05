# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-02-04 21:02:47
# @Last Modified by:   krocki
# @Last Modified time: 2017-02-04 21:02:54

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head:
            return False

        ptr1 = head
        ptr2 = head
        
        while (ptr1 and ptr2):
            
            if ptr1: ptr1 = ptr1.next
            if ptr2: ptr2 = ptr2.next
            if ptr2: ptr2 = ptr2.next
            
            if ptr1 != None and ptr1 == ptr2: return True
        
        return False
