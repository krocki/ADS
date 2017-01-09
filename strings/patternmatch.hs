-- @Author: krocki
-- @Date:   2017-01-08 22:01:47
-- @Last Modified by:   krocki
-- @Last Modified time: 2017-01-08 22:20:02

{-
    Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.

    Examples:

    Input:  txt[] = "THIS IS A TEST TEXT"
            pat[] = "TEST"
    Output: Pattern found at index 10

    Input:  txt[] =  "AABAACAADAABAABA"
            pat[] =  "AABA"
    Output: Pattern found at index 0
            Pattern found at index 9
            Pattern found at index 12
-}

import Data.List

-- #1 - naive
-- how it works:
-- match "abcdbc" "bc" == [1,4]

-- inits (tails input) == [["","a","ab","abc","abc
-- d","abcdb","abcdbc"],["","b","bc","bcd","bcdb",
-- "bcdbc"],["","c","cd","cdb","cdbc"],["","d","db
-- ","dbc"],["","b","bc"],["","c"],[""]] 

-- isFound == 
-- [[False,False,False,False,False,False,False]
-- ,[False,False,True,False,False,False],[False,Fa
-- lse,False,False,False],[False,False,False,False
-- ],[False,False,True],[False,False],[False]]

match :: String -> String -> [Int]
match input pattern = [pos | pos <- [0..length input-1], or (isFound !! pos)]
    where isFound = map (\x -> map (==pattern) (inits x)) (tails input)
