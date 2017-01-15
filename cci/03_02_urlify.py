# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-14 19:15:43
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-14 19:56:15

#urlify - replace space with %20

def nowhitespace(k):

	if k == ' ': 
		return '%20'
	else: 
		return k

def urlify(str):

	list_str = list(str);
	processed = [nowhitespace(k) for k in list_str]
	# return reduce(lambda x,y: x + y, processed)
	return ''.join(processed)


print urlify("abc ads asdddd")
