-- @Author: krocki
-- @Date:   2016-12-16 20:51:10
-- @Last Modified by:   krocki
-- @Last Modified time: 2016-12-17 10:46:50

-- all nonempty subsequences
-- subsequences :: [a] -> [[a]]

heads :: [a] -> [[a]]
heads [] = [[]]
heads [x] = [[x]]
heads (x:xs) = [x] : map (x:) (heads xs)

subsequences :: [a] -> [[a]]
subsequences [] = [[]]
subsequences [x] = [[x]]
subsequences (x:xs) = map (x:) (heads xs) ++ subsequences xs

-- all nonempty subsequences of length l

subsequences' :: [a] -> Int -> [[a]]
subsequences' [] _ = []
subsequences' (x:xs) l 
      | length xs >= (l-1) = [x:take (l-1) xs] ++ subsequences' xs l
      | otherwise = []

-- or take all subsequences and filter them to get only those of length l
subsequences'' :: [a] -> Int -> [[a]]
subsequences'' (x:xs) l  = filter (\x -> length x == l) (subsequences (x:xs))

main = do
    print (subsequences'' "test_sequence" 4)
    print (subsequences' "test_sequence" 4)
    print (subsequences "test_sequence")