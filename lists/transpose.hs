-- @Author: krocki
-- @Date:   2016-12-23 21:17:28
-- @Last Modified by:   krocki
-- @Last Modified time: 2016-12-24 10:02:54

-- transpose [[1..4], [5..8], [9..12]]
-- = [[1,5,9],[2,6,10],[3,7,11],[4,8,12]]

transpose :: [[a]] -> [[a]]
transpose [] = []
transpose ([] : xss) = transpose xss
transpose ((x:xs) : xss) = (x: [h | (h:_) <- xss]) : transpose (xs : [t | (_:t) <- xss])

-- 1. take head element from the first list - x
-- 2. append the remaining heads from xss using list comprehension x: [h | (h:_) <- xss]
-- [1,5,9]
-- 3. process remaining tails recursively and append
-- [2,6,10], [3,7,11] ...