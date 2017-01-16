# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-14 19:18:56
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-14 20:04:38

#implement a stack with push, pop and min with O(1)

			stack [], 		minstack = []
insert 3	stack [3], 		minstack = [3]
insert 5	stack [5,3] 	minstack = [3,3]
insert 1	stack [1,5,3], 	minstack = [1,3,3] or [(1,1), (5,3), (3,3)]

push v = push v s, push min(minstack peek, v)
