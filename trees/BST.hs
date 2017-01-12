-- @Author: krocki
-- @Date:   2016-12-18 19:31:49
-- @Last Modified by:   krocki
-- @Last Modified time: 2017-01-11 16:07:19

-- binary search tree


data Tree = NULL | Node Int Tree Tree deriving (Eq, Show)

isBST n@(Node v l r) = isBST' n (-1000000) 1000000 

isBST' NULL _ _ = True
isBST' (Node v l r) minval maxval
    | v >= maxval || v <= minval = False
    | otherwise = (isBST' l minval v) && (isBST' r v maxval)

-- a - not BST
--      1
--    /   \
--   0     2
--  / \   /  \
-- 3   4 5   11

-- b - BST
--      4
--    /   \
--   2     6
--  / \   /  \
-- 1   3 5    7

-- c - not BST
--      4
--    /   \
--   2     4

main = do
    let a = Node 1 (Node 0 (Node 3 NULL NULL) (Node 4 NULL NULL)) (Node 2 (Node 5 NULL NULL) (Node 11 NULL NULL))
    let b = Node 4 (Node 2 (Node 1 NULL NULL) (Node 3 NULL NULL)) (Node 6 (Node 5 NULL NULL) (Node 7 NULL NULL))
    let c = Node 4 (Node 2 NULL NULL) (Node 4 NULL NULL)

    print (isBST a)
    print (isBST b)
    print (isBST c)
