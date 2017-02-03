# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-02-03 12:39:01
# @Last Modified by:   krocki
# @Last Modified time: 2017-02-03 12:39:03

arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = []
            
        n = num
        count = 0
                
        while (count < 8):
            count = count + 1
            d = n & 15
            print n
            result += arr[d]
            n = n >> 4
            if (n == 0): break
        
        result.reverse()
        result = "".join(result)
        
        return result
