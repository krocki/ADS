# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-22 20:21:37
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-22 20:32:10

# You have a list of integers, and for each index
# you want to find the product of every integer
# except the integer at that index. Write a
# function
# get_products_of_all_ints_except_at_index() that
# takes a list of integers and returns a list of
# the products.

# For example, given:

#   [1, 7, 3, 4]

# your function would return:

#   [84, 12, 28, 21]

# by calculating:

#   [7*3*4, 1*3*4, 1*7*4, 1*7*3]

# Do not use division in your solution.

arr = [1, 7, 3, 4]

products = [None] * len(arr)

product = 1
for i in range(0, len(arr)):
	products[i] = product
	product *= arr[i]

product = 1
for i in range(len(arr)-1, -1, -1):
	products[i] *= product
	product *= arr[i]

print products
