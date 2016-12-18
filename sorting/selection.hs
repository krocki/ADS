-- @Author: krocki
-- @Date:   2016-12-18 14:38:21
-- @Last Modified by:   krocki
-- @Last Modified time: 2016-12-18 14:58:26

import Data.List

-- remove the smallest element, put it at the beginning, sort the rest and append

selectionSort :: (Ord a) => [a] -> [a]
selectionSort [] = []
selectionSort x = min : selectionSort (rest)
               where 
               	  min = minimum x
               	  rest = delete min x
