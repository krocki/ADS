-- @Author: krocki
-- @Date:   2017-01-08 13:13:44
-- @Last Modified by:   krocki
-- @Last Modified time: 2017-01-09 20:45:21

{- http://techieme.in/shortest-path-using-dijkstras-algorithm/

    1 2 3 4 5 6
    
1   0 3 4 2 x x
2   3 0 4 x 2 x
3   4 4 0 x 6 x
4   2 x x 0 1 4
5   x 2 6 1 0 2
6   x x x 4 2 0
-}

import Data.List
import Data.Map


inf = 1/0

-- PROTOTYPE

costs :: [[Float]]
costs = [[  0,   3,   4,   2, inf, inf], 
         [  3,   0,   4, inf,   2, inf], 
         [  4,   4,   0, inf,   6, inf], 
         [  2, inf, inf,   0,   1,   4], 
         [inf,   2,   6,   1,   0,   2], 
         [inf, inf, inf,   4,   2,   0]]

num_vertices = length costs

cost i j = if i <= j then costs !! i !! j else cost j i

lowest d unvisited = Data.List.foldl1 (\(k, v) (k',v') -> 
                                if v < v' && k `elem` unvisited 
                                then (k, v) 
                                else (k',v')) (Data.Map.toList d)

shortest distances unvisited =  if length unvisited > 2 
                                then shortest distances' (Data.List.delete (fst k) unvisited)
                                else distances'
                                where k = lowest distances unvisited
                                      distances' = updateDistances' (fst k) distances

val (Just a) = a

updateDistances' i distances = Data.Map.mapWithKey (\k v -> min (val (dk k)) (new k)) distances
                                where 
                                    dk k = Data.Map.lookup k distances
                                    di = Data.Map.lookup i distances
                                    new k = cost i k + val di

main = do
    let src = 0
        distances = fromList [(v, if v == src then 0 else inf) | v <- [0..num_vertices-1]]

    print (shortest distances [0..5])

