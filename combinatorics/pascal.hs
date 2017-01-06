-- @Author: krocki
-- @Date:   2017-01-05 20:29:46
-- @Last Modified by:   krocki
-- @Last Modified time: 2017-01-05 20:37:41

-- start with [1]
-- 1. zip [0, 1] + [1, 0] = [1,1]
-- 2. zip [0, 1, 1] + [1,1,0] = [1,2,1]
-- 3. zip [0,1,2,1] + [1,2,1,0] = [1,3,3,1]
-- etc

pascal :: [[Int]]
pascal = iterate (\x -> zipWith (+) ([0] ++ x) (x ++ [0])) [1]

main = do
    let triangle = take 5 pascal
    print triangle