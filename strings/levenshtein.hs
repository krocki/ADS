-- @Author: krocki
-- @Date:   2017-01-21 18:22:30
-- @Last Modified by:   krocki
-- @Last Modified time: 2017-01-21 20:49:58

{-

Compute Levenshtein distance between two strings.

Description

Given two strings, compute the Levenshtein
distance between them i.e. the minimum number of
edits required to convert one string into the
other.

For example, the Levenshtein distance between
"kitten" and "sitting" is 3.

The minimum steps required to transform the former
into latter are:

kitten → sitten (substitution of "s" for "k")
sitten → sittin (substitution of "i" for "e")
sittin → sitting (insertion of "g" at the end)
-}

-- some base cases
levenshtein_distance x [] = length x
levenshtein_distance [] x = length x

-- 0. simple recursion
levenshtein_distance x y
                | x == y = 0
                | otherwise = minimum [d1, d2, d3]
                where d1 = levenshtein_distance (init x) y + 1
                      d2 = levenshtein_distance x (init y) + 1
                      cost = if last x == last y then 0 else 1
                      d3 = levenshtein_distance (init x) (init y) + cost 

-- TODO:

-- 1. with memoization

-- 2. with DP
