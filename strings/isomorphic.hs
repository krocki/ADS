-- @Author: krocki
-- @Date:   2017-01-10 22:37:37
-- @Last Modified by:   krocki
-- @Last Modified time: 2017-01-11 11:57:14

-- Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic if the characters in s can be replaced to get t.

-- For example,"egg" and "add" are isomorphic, "foo" and "bar" are not.

isomorphic [] [] = True
isomorphic a b
    | length a /= length b = False
    | otherwise = isomorphic' a b [] && isomorphic' b a []

isomorphic' [] [] _ = True
isomorphic' (a:as) (b:bs) mapped
    | a /= b = if  a `elem` mapped then False else isomorphic' (map (\x -> if x == a then b else x) as) bs (b:mapped)
    | otherwise = isomorphic' as bs mapped
