-- @Author: krocki
-- @Date:   2017-01-20 17:51:32
-- @Last Modified by:   krocki
-- @Last Modified time: 2017-01-20 20:14:08

import Data.List

-- compute prefix sums (cumulative sum)

-- for i=1:1:N : sum[i] = sum[i-1] + x[i]
-- example: prefix_sums [1,2,3,4,5,6,7,8] = [1,3,6,10,15,21,28,36]

-- naive, O(N)
prefix_sums :: [Int] -> [Int]
prefix_sums [] = []
prefix_sums xs = prefix_sums a ++ [e + (sum a)]
                  where a = init xs
                        e = last xs

pairs :: [Int] -> [[Int]]
pairs [] = []
pairs (x:y:xs) = [x,y]:(pairs xs)

-- more complex recursive solution, O(logN)
cumsum :: [Int] -> [Int]
cumsum (q:[]) = [q]
cumsum (p:q:[]) = [p, p+q]
cumsum q = concat (zipWith (\x z -> fmap (+z) x) a c)
            where a = fmap (cumsum) (pairs q)
                  l = [0] ++  init (map (\x -> last x) a)
                  c = cumsum l

