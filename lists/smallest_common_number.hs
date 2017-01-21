-- @Author: krocki
-- @Date:   2017-01-20 20:48:59
-- @Last Modified by:   krocki
-- @Last Modified time: 2017-01-21 14:20:06

-- Given three integer arrays sorted in ascending
-- order, find the smallest number that is common
-- in all three arrays. For example, let's look at
-- the below three arrays. Here 6 is the smallest
-- number that's common in all the arrays.

-- scn a b c == 6
-- scn :: [Int] -> [Int] -> [Int] -> Int

-- TODO: if there is no common value - return Nothing
-- of of the lists reaches [] -> no common value
-- include Maybe

scn (a:as) (b:bs) (c:cs) val 
            | a == val && b == val && c == val = val
            | otherwise = scn a' b' c' val'
                where a' = if a < val then as else (a:as)
                      b' = if b < val then bs else (b:bs)
                      c' = if c < val then cs else (c:cs)
                      val' = maximum [a, b, c]

main = do
        let a = [6, 7, 10, 25, 30, 63, 64]
            b = [-1, 4, 5, 6, 7, 8, 10]
            c = [1, 6, 10]
            s = scn a b c (maximum [head a, head b, head c])
        print s
