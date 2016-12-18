-- @Author: krocki
-- @Date:   2016-12-17 19:34:02
-- @Last Modified by:   krocki
-- @Last Modified time: 2016-12-17 19:55:35

import System.Random
import Data.List

main = do
    seed <- newStdGen
    let unsorted = randomList (50, 1, 1000) seed
        sorted = insertionSort unsorted
    putStrLn $ "Before sorting: \n" ++ show unsorted
    putStrLn $ "After sorting: \n" ++ show sorted

randomList :: (Int, Int, Int) -> StdGen -> [Int]
randomList (n, min, max) gen = take n (randomRs (min,max) gen)

-- insertion of x into a sorted array
insertion x [] = [x]
insertion x (sortedhead:sortedtail)
            | sortedhead < x = sortedhead:(insertion x sortedtail)
            | otherwise = x:sortedhead:sortedtail

-- insertionSort
insertionSort :: (Ord a) => [a] -> [a]
insertionSort [] = []
insertionSort [x] = [x]
insertionSort (x:xs) = insertion x (insertionSort xs)

