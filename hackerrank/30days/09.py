-- @Author: krocki
-- @Date:   2017-01-04 15:10:23
-- @Last Modified by:   krocki
-- @Last Modified time: 2017-01-04 15:10:27

def factorial(n):
    if n == 1: return 1
    else: return n * factorial(n-1)
    
n = input()
print factorial(n)