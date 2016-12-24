-- @Author: krocki
-- @Date:   2016-12-23 19:20:32
-- @Last Modified by:   krocki
-- @Last Modified time: 2016-12-23 20:13:52

import Data.List

-- xs is a sorted list
combinations' :: (Ord a) => [a] -> Int -> [[a]]
combinations' [] _ = [[]]
combinations' _ 0 = [[]]
combinations' xs elems = [xs !! i:rest | i <- [0..(length xs) - elems], 
                          rest <- combinations (drop (i+1) xs) (elems-1)]

-- first sort and remove duplicates
combinations :: (Ord a) => [a] -> Int -> [[a]]
combinations xs elems = combinations' (nub (sort xs)) elems