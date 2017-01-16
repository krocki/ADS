# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-14 19:16:49
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-14 20:01:25

#remove middle node in a list without access to head

['a', 'b', 'c', 'd', 'e']

# remove 'c' -> 'c'->next == 'd': 'c'->next = 'd'->next, 'c'.val = 'd'.val, free(d)
