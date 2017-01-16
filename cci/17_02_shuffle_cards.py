# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-14 19:23:03
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-15 14:51:39

# write a method to shuffle a deck of cards, each permutation has to be equally likely
# assume we have a RNG

import random

['a', 'b', 'c'] - take 1st with prob 1/3 [a], [b], [c], remove from list

a + [b, c] - take snd with prob 1/2 [ab] = 1/6, [ac] = 1/6

[abc] 1/6 [acb] 1/6
[bac] 1/6 [bca] 1/6
[cab] 1/6 [cba] 1/6

f(list) = [x = choose element from list randomly, remove from list,  x:f(del x lst)]
