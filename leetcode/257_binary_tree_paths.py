# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-19 19:04:14
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-19 19:04:17

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    
    def binaryTreePaths(self, root):
        
        paths = []
        
        if root:
            
            if not root.left and not root.right:
                paths.append(str(root.val))
                
            if root.left:
                
                for i in self.binaryTreePaths(root.left):
                    paths.append((str(root.val) + "->" + i))
                    
            if root.right:
                
                for i in self.binaryTreePaths(root.right):
                    paths.append((str(root.val) + "->" + i))
            
        return paths
        
