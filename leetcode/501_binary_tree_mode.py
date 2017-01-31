# -*- coding: utf-8 -*-
# @Author: Kamil Rocki
# @Date:   2017-01-31 11:00:37
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-31 11:48:13

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

max_cnt = 0
    
def get_mode(root, node, vals):
    
    global max_cnt
    
    if node:

        vals[node.val] = vals.get(node.val, 0) + 1

        if node.left: vals = get_mode(root, node.left, vals)
        if node.right: vals = get_mode(root, node.right, vals)
        
        max_cnt = max(max_cnt, vals.get(node.val, 0))
        if node == root: vals = {key: value for key, value in vals.items() if value == max_cnt}
        
            
    return vals
    
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        global max_cnt
        max_cnt = 0
        vals={}
        m = get_mode(root, root, vals)
        res = []
        for i in m:
            res += [i]
        
        return res
