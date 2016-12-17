-- @Author: krocki
-- @Date:   2016-12-16 18:29:38
-- @Last Modified by:   krocki
-- @Last Modified time: 2016-12-16 20:07:58

import System.Random
import Data.List

main = do
    seed <- newStdGen
    let unsorted = randomList (100, 1, 1000) seed
        sorted = quicksort unsorted
    putStrLn $ "Before sorting: \n" ++ show unsorted
    putStrLn $ "After sorting: \n" ++ show sorted

randomList :: (Int, Int, Int) -> StdGen -> [Int]
randomList (n, min, max) gen = take n (randomRs (min,max) gen)

-- let's choose 1st element to be the pivot (x)
-- we put this pivot in the middle, all elements < x to the left,
-- all elements >= x to the right and process left and right
-- recursively until []

quicksort:: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) = quicksort left  ++ [x] ++ quicksort right
                   where left = [e | e <- xs, e < x]
                         right = [e | e <- xs, e >= x]
