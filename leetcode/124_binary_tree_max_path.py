# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-19 15:42:07
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-19 15:42:28

# Given a binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

# For example:
# Given the below binary tree,

#        1
#       / \
#      2   3
# Return 6.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
            
class Solution(object):
    
    maxval = None
    
    def maxPathSum(self, root):
        self.maxval = -9999999999
        self.maxPaths(root)
        return self.maxval;
        
    def maxPaths(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            l = max(0, self.maxPaths(root.left))
            r = max(0, self.maxPaths(root.right))
            self.maxval = max(self.maxval, root.val + l + r)
            return root.val + max(l, r);
        else:
            return 0
