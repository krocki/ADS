-- @Author: krocki
-- @Date:   2016-12-16 20:51:10
-- @Last Modified by:   krocki
-- @Last Modified time: 2016-12-16 21:25:32

-- subsequences :: [a] -> [[a]]

heads [] = [[]]
heads [x] = [[x]]
heads (x:xs) = [x] : map (x:) (heads xs)

subsequences [] = [[]]
subsequences [x] = [[x]]
subsequences (x:xs) = map (x:) (heads xs) ++ subsequences xs

main = do
    print (subsequences "test_sequence")