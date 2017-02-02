# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-02-01 16:31:24
# @Last Modified by:   krocki
# @Last Modified time: 2017-02-01 16:31:26

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            if head.next:
                head.next = self.deleteDuplicates(head.next)
                if head.val == head.next.val:
                    head = head.next
                
        
        return head
