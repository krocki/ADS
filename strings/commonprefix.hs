-- @Author: krocki
-- @Date:   2017-01-10 22:34:18
-- @Last Modified by:   krocki
-- @Last Modified time: 2017-01-11 12:13:01

-- Write a function to find the longest common prefix string amongst an array of strings.

-- longestprefix ["abc", "abcde", "ab"] == "ab"

longestprefix strings = longestprefix' strings []

longestprefix' (x:xs) [] = longestprefix' xs x
longestprefix' [] p = p
longestprefix' (x:xs) p = longestprefix' xs (trimprefix p x)

trimprefix [] _ = []
trimprefix _ [] = []
trimprefix (p:ps) (x:xs)
    | x == p = p : trimprefix ps xs
    | otherwise = []

