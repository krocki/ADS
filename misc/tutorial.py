# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-12 22:07:06
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-13 13:38:39

# list comprehension in python

def f(i,s):
	return '%d - %s' % (i, s)

s = ['a', 'b', 'c']

print [f(i,s) for i,s in enumerate(s)]


#iterators
i = iter('abcd')

print i.next()
print i.next()
print i.next()
t = tuple(i)
print t
# print i.next() StopIteration exception

#generators

# Generator expressions are surrounded by parentheses (“()”) 
# and list comprehensions are surrounded by square brackets (“[]”).
# Generator expressions have the form:

# ( expression for expr in sequence1
#              if condition1
#              for expr2 in sequence2
#              if condition2
#              for expr3 in sequence3 ...
#              if condition3
#              for exprN in sequenceN
#              if conditionN )

def fib():
	a, b = 0, 1
	while True:
		yield b
		a,b = b, a + b	

seq = fib()

print [seq.next() for i in range(10)]

it = (x**2 for x in range(10))
for e in it:
	print e

from itertools import groupby
def compress(data):
	return ((len(list(group)), name)
		for name, group in groupby(data))

print list(compress('get uuuuuuuuuuuuuuuuuup'))
