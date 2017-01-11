-- @Author: krocki
-- @Date:   2017-01-10 22:49:52
-- @Last Modified by:   krocki
-- @Last Modified time: 2017-01-11 11:30:27

-- Implement wildcard pattern matching with support for '?' and '*'.

-- return String(s) which matches the pattern
-- regexmatch :: [String] -> String -> [String]
-- regexmatch [] _ = []
-- regexmatch (x:xs) exp
--     | match x exp = x:regexmatch xs exp

import Data.List

wildcardmatch [] [] = True
wildcardmatch [] _ = False
wildcardmatch (e:es) [] = if e == '*' && es == [] then True else False

wildcardmatch exp@(e:es) str@(x:xs)
            | exp == str = True
            | e == x || e == '?' = wildcardmatch es xs
            | e == '*' = or [wildcardmatch (xx ++ es) xs | xx <- [replicate n '?' | n <- [0..(length xs)]]]
            | otherwise = False

-- match "123456667" "*456*" == True
-- match "123456667" "*454*" == False
match str exp = or . map (\x -> or . map (\y -> (wildcardmatch exp y)) . inits $ x). tails $ str


