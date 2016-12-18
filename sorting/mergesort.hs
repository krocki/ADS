-- @Author: krocki
-- @Date:   2016-12-16 20:46:04
-- @Last Modified by:   krocki
-- @Last Modified time: 2016-12-17 20:28:42

-- merge two sorted lists
merge :: Ord a => [a] -> [a] -> [a]
merge xs [] = xs
merge [] ys = ys
merge (x:xs) (y:ys)
      | (x <= y)  = x:(merge xs (y:ys))
      | otherwise = y:(merge (x:xs) ys)

mergesort :: Ord a => [a] -> [a]
mergesort [] = []
mergesort [x] = [x]
mergesort x = merge (mergesort fst) (mergesort snd)
            where (fst, snd) = splitAt (length x `div` 2) x
