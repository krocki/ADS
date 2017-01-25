# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-24 20:44:05
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-24 20:44:07

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def reverseList(self, head):
        
        if not head or not head.next:
            return head
        else:
            tail = head.next
            new_head = self.reverseList(head.next)
            tail.next = head
            head.next = None
            return new_head
