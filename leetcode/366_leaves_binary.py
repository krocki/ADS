# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-30 21:02:21
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-30 21:02:23

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def is_leaf(node):
    if node:
        return not node.left and not node.right
    else:
        return False
        
def remove_leaves(node):
    
    s = []
    
    if node:
        
        if not is_leaf(node):
            node.left, l = remove_leaves(node.left)
            node.right, r = remove_leaves(node.right)
            s = l + r
        else:
            s = [node.val]
            node = None      
    return node, s
            
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        n = root
        
        while n:
            n, r = remove_leaves(root)
            result += [r]
        
        return result
