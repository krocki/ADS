# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-14 19:22:11
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-14 20:18:28

# book -> word frequencies, what if we need to run multiple times?

txt = "abc abc the the of the abb abb"

def frequencies(str):

	return rle(sorted(str.split(' ')))
	# TODO: sort by snd, descending, take top results
def rle(words):

	result = []
	counter = 1

	for i in range(1, len(words)):
		if words[i-1] == words[i]:
			counter += 1
		else:
			result.append((words[i-1], counter))
			counter = 1
	
	result.append((words[-1], counter))

	return result

print frequencies(txt)
