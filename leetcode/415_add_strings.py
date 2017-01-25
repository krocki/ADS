# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-24 21:05:22
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-24 21:05:23

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        k = len(num1)
        l = len(num2)
        
        if l > k: return self.addStrings(num2, num1)
        
        result = ""
        carry = 0
        i = 0
        
        while i < k or carry:
            
            sum = carry
            
            if i < k:
                sum += int(num1[k-i-1])
            if i < l:
                sum += int(num2[l-i-1])
                 
            digit = sum %10
            carry = sum / 10
            result = str(digit) + result
            i += 1
            
        return result
