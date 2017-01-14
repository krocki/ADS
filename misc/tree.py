# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-13 13:41:48
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-13 19:37:04

# A recursive generator that generates Tree leaves in in-order.
def inorder(t):
    if t:
        for x in inorder(t.left):
            yield x

        yield t.label

        for x in inorder(t.right):
            yield x
