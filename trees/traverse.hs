-- @Author: krocki
-- @Date:   2016-12-25 21:59:38
-- @Last Modified by:   krocki
-- @Last Modified time: 2016-12-26 14:23:11

-- enumerate all paths from root to leaves

data Tree = NULL | Node Int Tree Tree deriving (Eq, Show)

-- enumerates paths in a binary tree
enumeratePaths (Node v NULL NULL) = [[v]]
enumeratePaths (Node v l r) = 
    [v:paths | x <- [l,r], paths <- enumeratePaths x]

--     0
--    / \
--   1   2
--  / \
-- 3   4
--    / \
--   5   6
--      / \
--     7   8
--        / \
--       9  10

main = do
    let root = Node 0 (Node 1 (Node 3 NULL NULL) (Node 4 (Node 5 NULL NULL) (Node 6 (Node 7 NULL NULL) (Node 8 (Node 9 NULL NULL) (Node 10 NULL NULL))))) (Node 2 NULL NULL)
    print (enumeratePaths root)


