-- @Author: krocki
-- @Date:   2016-12-16 20:51:21
-- @Last Modified by:   krocki
-- @Last Modified time: 2016-12-19 19:09:19


import Data.List

-- input: a list, output: list of lists

permutation :: (Eq a) => [a] -> [[a]]
permutation [] = [[]]
permutation xs = [x:rest | x <- xs, rest <- permutation (delete x xs)]

-- using list comprehension, for each elements in xs:
-- keep one element fixed (x <- xs), put at the beginning of a new list
-- (x:rest) and append rest = permutation (all remaining symbols)