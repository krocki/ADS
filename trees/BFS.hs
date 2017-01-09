-- @Author: krocki
-- @Date:   2017-01-08 22:22:24
-- @Last Modified by:   krocki
-- @Last Modified time: 2017-01-09 12:27:26

data Tree = NULL | Node Int Tree Tree deriving (Eq, Show)

-- 2nd argument of bfs is a list of nodes to be examined
bfs :: Int -> [Tree] -> [[Int]]
bfs k [] = []
bfs k ((Node v l r):rest) = if v == k then [[v]] else
    [v:paths | let x = rest ++ (filter (/= NULL) [l,r]), paths <- bfs k x]

--     0
--    / \
--   1   2
--  / \   \
-- 3   4  11
--    / \
--   5   6
--      / \
--     7   8
--        / \
--       9  10
--      /
--     11 (Two "11"s on purpose)

main = do
     let root = Node 0 (Node 1 (Node 3 NULL NULL) (Node 4 (Node 5 NULL NULL) (Node 6 (Node 7 NULL NULL) (Node 8 (Node 9 (Node 11 NULL NULL) NULL) (Node 10 NULL NULL))))) (Node 2 NULL (Node 11 NULL NULL))
     print (bfs 0 [root])
     print (bfs 2 [root])
     print (bfs 8 [root])
     print (bfs 5 [root])
     print (bfs 11 [root])
     print (bfs 12 [root])

{-  output
    [[0]]
    [[0,1,2]]
    [[0,1,2,3,4,11,5,6,7,8]]
    [[0,1,2,3,4,11,5]]
    [[0,1,2,3,4,11]]
    []
-}
