# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-23 22:11:36
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-23 22:19:51

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    num = 0
    last_num = 0

    for i in range(len(s)-1,-1, -1):
		if d[s[i]] >= last_num:
			num += d[s[i]]
		else:
			num -= d[s[i]]

		last_num = d[s[i]]

    return num

print romanToInt("DMMVIII")
