-- @Author: krocki
-- @Date:   2017-01-09 10:50:43
-- @Last Modified by:   krocki
-- @Last Modified time: 2017-01-09 12:10:30

data Tree = NULL | Node Int Tree Tree deriving (Eq, Show)

dfs k (Node v l r) = if v == k then [[v]] else 
    [v:paths | x <- filter (/= NULL) [l,r], paths <- dfs k x]

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
    print (dfs 0 root)
    print (dfs 2 root)
    print (dfs 8 root)
    print (dfs 5 root)
    print (dfs 11 root)

{-  output
    [[0]]
    [[0,2]]
    [[0,1,4,6,8]]
    [[0,1,4,5]]
    [[0,1,4,6,8,9,11],[0,2,11]]
-}
