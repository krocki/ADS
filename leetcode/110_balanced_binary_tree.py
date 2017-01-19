# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-19 12:42:38
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-19 12:42:44

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def depth(root):
    
        if root:
            return 1 + max(depth(root.left), depth(root.right))
        else:
            return 0
            
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            if abs(depth(root.left) - depth(root.right)) > 1: 
                return False
            else: 
                return self.isBalanced(root.left) and self.isBalanced(root.right)

        else:
            return True
            
