# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-14 19:15:43
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-15 15:06:58

#urlify - replace space with %20
#TODO: write in C

# def nowhitespace(k):

# 	if k == ' ': 
# 		return '%20'
# 	else: 
# 		return k

# def urlify(str):

# 	list_str = list(str);
# 	processed = [nowhitespace(k) for k in list_str]
# 	# return reduce(lambda x,y: x + y, processed)
# 	return ''.join(processed)

def count_spaces(array, l):

	counter = 0
	
	for i, a in enumerate(array):
		if i >= l: break
		if a == ' ': counter += 1

	return counter

def urlify (array, l):

	num_spaces = count_spaces(array, l)

	new_length = (l - num_spaces) + 3 * num_spaces

	k = l

	for i in range(new_length-1, 0, -1):
		array[i] = array[k]
		print array[k]
		k = k - 1
		if (array[k] == ' '):
			array[i-2] = '%'
			array[i-1] = '2'
			array[i] = '0'
			i = i - 2

	return array

print urlify("abc ads asdddd      ", 14)
