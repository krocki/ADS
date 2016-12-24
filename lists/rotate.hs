-- @Author: krocki
-- @Date:   2016-12-23 18:22:55
-- @Last Modified by:   krocki
-- @Last Modified time: 2016-12-23 18:46:22

-- rotate a list n places to the left

-- examples:
-- rotate ['a','b','c','d','e','f','g','h'] 3
-- "defghabc"
-- rotate ['a','b','c','d','e','f','g','h'] (-2)
-- "ghabcdef"

rotate :: [a] -> Int -> [a]
rotate xs n 
        | n >= 0 = drop n xs ++ take n xs
        | otherwise = drop (length xs + n) xs ++ take (length xs + n) xs