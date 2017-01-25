# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-25 11:55:47
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-25 11:55:49

def fizzorbuzz(x):
    s = ""
    if x % 3 == 0: s += "Fizz"
    if x % 5 == 0: s += "Buzz"
    if x % 5 != 0 and x % 3 != 0:
        s = str(x)
    
    return s
    
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [fizzorbuzz(i) for i in range(1,n+1)]
