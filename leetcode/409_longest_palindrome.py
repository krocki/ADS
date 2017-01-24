# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-24 15:48:37
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-24 15:54:54

def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    d = {}
    
    for x in s:
        k = d.get(x)
        if k:
            d[x] += 1
        else:
            d[x] = 1
    
    cnt = 0  
    add = 0
    
    for k,v in d.iteritems():
    	r = v % 2
    	n = v / 2
    	cnt += n*2
    	if r == 1:
    		add = 1

    cnt += add

    return cnt

print longestPalindrome("abccccdd")
