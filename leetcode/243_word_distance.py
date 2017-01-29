# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-01-26 11:40:17
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-01-26 20:40:36

def shortestDistance(words, word1, word2):
	"""
	:type words: List[str]
	:type word1: str
	:type word2: str
	:rtype: int
	"""

	d = len(words)
	w1 = len(words)
	w2 = len(words)

	for i,x in enumerate(words):
		if x == word1:
			w1 = i
			d = min(d, abs(w1-w2))
		if x == word2:
			w2 = i
			d = min(d, abs(w1-w2))

	return d

print shortestDistance(["a","c","a","b"], "a", "b")