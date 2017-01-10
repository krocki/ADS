-- @Author: krocki
-- @Date:   2017-01-09 21:38:24
-- @Last Modified by:   krocki
-- @Last Modified time: 2017-01-10 15:45:54

-- get most frequent words

import Data.Char
import Data.List
import Data.Function (on)

txt = "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do:  once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, `and what is the use of a book,' thought Alice `without pictures or conversation?'"

-- ["a","alice","alice" == [("a", 1), ("alice",2)]
countruns :: [String] -> Int -> [(String, Int)]
countruns [] _ = []
countruns (x:[]) n = [(x,n)]
countruns (x:xs) n
    | head xs == x = countruns xs (n+1)
    | otherwise = (x,n):countruns xs 1

--sort tuple
tuplesort xs = sortBy (compare `on` snd) xs

main = do
    let topwords = take 10 (reverse (tuplesort (countruns (sort (words (map toLower txt))) 1)))
    print topwords
