-- @Author: krocki
-- @Date:   2016-12-20 20:11:04
-- @Last Modified by:   krocki
-- @Last Modified time: 2016-12-20 21:29:57

-- run length encoding

encode :: String -> String
encode x = encode' x 1

encode' :: String -> Int -> String
encode' (x:[]) acc = [x] ++ show acc
encode' (x:xs) acc
          | x == head xs = encode' xs (acc+1)
          | otherwise = [x] ++ (show acc) ++ (encode' xs 1)

-- "aaaaaabbbbbbbcccccccdefghhhhhhhhhhhhhhhhh"
--  -> "a6b7c7d1e1f1g1h17"

main = do
    let result = encode "aaaaaabbbbbbbcccccccdefghhhhhhhhhhhhhhhhh"
    print result
