# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-01-25 19:27:09
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-01-25 19:36:35
def generatePossibleNextMoves(s):

	result = []

	for i in range(1,len(s)):
		if s[i] == s[i-1] == '+':
			result.append(s[:i-1] + "--" + s[i+1:])

	return result


print generatePossibleNextMoves("++++")
print generatePossibleNextMoves("-++-")