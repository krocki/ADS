# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-02-06 16:56:28
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-02-06 16:56:30

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        stack = []
        
        for i in s:
            if len(stack) > 0:
                last = stack[0]
                if last == '[' and i == ']' or last == '{' and i == '}' or last == '(' and i == ')': 
                    stack = stack[1:]
                else:
                    stack.insert(0, i)
            else:
                stack.insert(0, i)
                
        return (len(stack) == 0)