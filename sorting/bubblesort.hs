-- @Author: krocki
-- @Date:   2016-12-16 20:06:19
-- @Last Modified by:   krocki
-- @Last Modified time: 2016-12-16 20:38:43

import System.Random
import Data.List

main = do
    seed <- newStdGen
    let unsorted = randomList (10, 1, 1000) seed
        sorted = bubblesort unsorted
    putStrLn $ "Before sorting: \n" ++ show unsorted
    putStrLn $ "After sorting: \n" ++ show sorted

randomList :: (Int, Int, Int) -> StdGen -> [Int]
randomList (n, min, max) gen = take n (randomRs (min,max) gen)

-- 'bubbled' is a list with the largest value on top
-- we need to run this n times (bubblesort (init bubbled) )
-- every time bubbling the value to the top [last bubbled]

bubblesort :: (Ord a) => [a] -> [a]
bubblesort [] = []
bubblesort [x] = [x]
bubblesort (x:y:rest) = bubblesort (init bubbled) ++ [last bubbled]
         where 
            (first, second) = compareAndSwap (x, y)
            bubbled = first : bubblesort (second:rest)

compareAndSwap :: (Ord a) => (a, a) -> (a, a)
compareAndSwap (x, y)
                | x < y = (x, y)
                | otherwise = (y, x)