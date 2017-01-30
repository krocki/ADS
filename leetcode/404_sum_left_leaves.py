# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-29 19:37:48
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-29 19:37:51

def isleaf(node):
    if node:
        return not node.left and not node.right
    else:
        return False
    
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        v = 0
        
        if root:
            
            if isleaf(root.left):
                v += root.left.val
            else:
                v += self.sumOfLeftLeaves(root.left)
            
            v += self.sumOfLeftLeaves(root.right)

        return v
