-- @Author: krocki
-- @Date:   2017-01-21 21:05:40
-- @Last Modified by:   krocki
-- @Last Modified time: 2017-01-22 20:16:50

{-
Given a list of day stock prices (integers for
simplicity), find the maximum single sell
profit.

We need to maximize the single buy/sell profit and
in case we can't make any profit, we'll try to
minimize the loss. For below examples, buy and
sell prices for making maximum profit are
highlighted. 
-}

max_profit :: (Ord a, Num a) => [a] -> a
max_profit (d:ds) = max_profit' ds d (head ds - d)

max_profit' :: (Ord a, Num a) => [a] -> a -> a -> a
max_profit' [] _ best_profit = best_profit
max_profit' (d:ds) buy best_profit = max_profit' ds buy' best_profit'
                where current_profit = d - buy
                      best_profit' = maximum [current_profit, best_profit]
                      buy' = minimum [d, buy]

main = do
    let a = [21, 12, 11, 9, 6, 3]
        b = [8, 5, 12, 9, 19, 1]
        profit = max_profit b
    print profit

