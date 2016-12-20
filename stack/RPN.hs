-- @Author: krocki
-- @Date:   2016-12-18 18:40:21
-- @Last Modified by:   krocki
-- @Last Modified time: 2016-12-19 21:00:38

-- Reverse Polish Notation calculator

-- input: string "2 3 +"

-- use stack to store intermediate results
--
-- process string:
--
-- if op - take 1 or 2 elements from the stack compute the results and put the results back
-- if num - push onto the stack

-- with a fold:

calculate expression = foldl (f) [] (words expression)
                        where f (a:b:acc) "*" = (a*b):acc
                              f (a:b:acc) "+" = (a+b):acc
                              f (a:acc) "log" = (log a):acc
                              f acc number = (read number):acc

-- 5 log 4 3 * 2 3 + + + = log 5 + (4 * 3) + (2 + 3) = 1.609437912434100 + 12
-- + 5 = 18.6094379124341

main = do
    let result = head (calculate "5 log 4 3 * 2 3 + + +")
    print result