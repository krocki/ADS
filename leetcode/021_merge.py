# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-02-07 20:19:04
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-02-07 20:19:06

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = []
        
        while l1 != None or l2 != None:
            print l1,l2
            if l1 != None and l2 != None:
                if l1.val > l2.val:
                    res.append(l2.val)
                    l2 = l2.next
                else:
                    res.append(l1.val)
                    l1 = l1.next
            else:
                if l1 != None:
                    res.append(l1.val)
                    l1 = l1.next
                else:
                    res.append(l2.val)
                    l2 = l2.next
        return res