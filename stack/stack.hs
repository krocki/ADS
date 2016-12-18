-- @Author: krocki
-- @Date:   2016-12-17 19:58:02
-- @Last Modified by:   krocki
-- @Last Modified time: 2016-12-17 20:05:04

type Stack a = [a]

push :: a -> Stack a -> Stack a
push item stack = item:stack

pop :: Stack a -> (a, Stack a)
pop [] = error " Empty stack !!! "
pop (x:xs) = (x, xs)