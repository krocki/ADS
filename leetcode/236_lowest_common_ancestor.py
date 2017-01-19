# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-19 13:08:50
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-19 13:08:55

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q): return root
        left,right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        
        if (left and right): return root
        elif left: return left
        else: return right
