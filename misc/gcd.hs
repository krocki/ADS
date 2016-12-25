-- @Author: krocki
-- @Date:   2016-12-24 20:46:24
-- @Last Modified by:   krocki
-- @Last Modified time: 2016-12-24 20:52:37

-- the Greatest Common Divisor (GCD) of two integers A and B is the largest
-- integer that divides both A and B. The Euclidean Algorithm is a technique
-- for quickly finding the GCD of two integers.

gcd' m 0 = m
gcd' m n 
    | n < m = gcd' n (m `mod` n)
    | otherwise = gcd' n m