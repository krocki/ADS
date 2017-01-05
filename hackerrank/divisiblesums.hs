-- @Author: krocki
-- @Date:   2017-01-04 16:01:52
-- @Last Modified by:   krocki
-- @Last Modified time: 2017-01-04 16:02:22

count_sums xs k = sum [1| i <- [0..(length xs-1)], j <- [0..(length xs-1)], (xs !! i + xs !! j) `mod` k == 0, i > j ]


main :: IO ()
main = do
    n_temp <- getLine
    let n_t = words n_temp
    let n = read $ n_t!!0 :: Int
    let k = read $ n_t!!1 :: Int
    a_temp <- getLine
    let a = map read $ words a_temp :: [Int]
        sums = count_sums a k
    print sums
