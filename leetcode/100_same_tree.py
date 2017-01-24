# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-23 21:33:22
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-23 21:33:24

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (not p and not q): return True
        elif p and q:
            if p.val != q.val: return False
            else: 
                l, r = self.isSameTree(p.left, q.left), self.isSameTree(p.right, q.right)
                return l and r
       
        return False
        
