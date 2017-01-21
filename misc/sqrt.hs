-- @Author: krocki
-- @Date:   2017-01-20 20:26:07
-- @Last Modified by:   krocki
-- @Last Modified time: 2017-01-20 20:46:01

{-
Given a double number, write a function to calculate its square root.

Square root of 16 is 4 (4 x 4 = 16). 
Square root of 17 is 4.123 
Square root of 2.25 is 1.5 

For this problem assume that the given number is always a
positive double number. -} 

-- mysqrt 2 == 1.4142135623842478

mysqrt :: Double -> Double
mysqrt x = mysqrt' x 0.0 x

-- O(logn) complexity: binary search to find n

mysqrt' :: Double -> Double -> Double -> Double
mysqrt' x low high 
        | abs(n*n - x) < eps = n
        | n*n < x = mysqrt' x n high
        | n*n > x = mysqrt' x low n
        where n = (high+low)/2
              eps = 1e-10
