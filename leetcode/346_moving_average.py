# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-01-25 15:29:14
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-01-25 15:56:23

class MovingAverage(object):

	def __init__(self, size):
		"""
		Initialize your data structure here.
		:type size: int
		"""
		self.current_window = []
		self.current_average = None        
		self.size = size

	def next(self, val):
		"""
		:type val: int
		:rtype: float
		"""
		l = len(self.current_window)

		self.current_window.append(val)

		if self.current_average:
			self.current_average = self.current_average * l + val

			if l == self.size:
				self.current_average -= self.current_window.pop(0)

			self.current_average /= float(min(self.size, l+1))

		else: self.current_average = val

		return self.current_average


size = 3
# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(size)
print obj.next(1)
print obj.next(2)
print obj.next(3)
print obj.next(4)