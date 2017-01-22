-- @Author: krocki
-- @Date:   2017-01-20 17:51:32
-- @Last Modified by:   krocki
-- @Last Modified time: 2017-01-21 17:10:38

import Data.List

-- compute prefix sums (cumulative sum)

-- for i=1:1:N : sum[i] = sum[i-1] + x[i]
-- example: prefix_sums [1,6,2,-1,0,7,8,9] = [1,7,9,8,8,15,23,32]

-- simple solution
prefix_sums :: [Int] -> [Int]
prefix_sums [] = []
prefix_sums xs = prefix_sums a ++ [e + (sum a)]
                  where a = init xs
                        e = last xs

pairs :: [Int] -> [[Int]]
pairs [] = []
-- pairs [1,2,3,4,5,6,7,8] == [[1,2], [3,4], [5,6], [7,8]]
pairs (x:y:xs) = [x,y]:(pairs xs)

-- more complex recursive map-reduce solution
cumsum :: [Int] -> [Int]
-- cumsum [1] == [1]
cumsum (q:[]) = [q]
-- cumsum [1,2] == [1,3]
cumsum (p:q:[]) = [p, p+q]

-- if length q > 2:

-- 1. split elements into groups of 2 and run cumsum of each pair (line 46)
-- q = [1,2,3,4] -> a = [cumsum [1,2], cumsum [3,4]] = [[1,3], [3,7]]

-- 2. for each item in a -> get last element of the previous pair (line 47)
-- [[1,3], [3,7]] -> [0, 3]

-- 3. run cum sum recursively on l (line 48)

-- 4. combine sums of pairs with prefix sums of last elements (line 45)
-- a <- [[1,3], [3,7]], c <- [0, 3], q == [1, 3, 6, 10]

cumsum q = concat (zipWith (\x z -> fmap (+z) x) a c)
            where a = fmap (cumsum) (pairs q)
                  l = [0] ++  init (map (\x -> last x) a)     
                  c = cumsum l

