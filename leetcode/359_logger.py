# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-25 12:15:39
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-25 14:53:24

class Logger(object):

	d = {}
	
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		
	def shouldPrintMessage(self, timestamp, message):
		"""
		Returns true if the message should be printed in the given timestamp, otherwise returns false.
		If this method returns false, the message will not be printed.
		The timestamp is in seconds granularity.
		:type timestamp: int
		:type message: str
		:rtype: bool
		"""
		k = self.d.get(message)
	   
		if k:
			print self.d[message]
			if self.d[message] + 10 < timestamp:
				self.d[message] = timestamp
				return True
			else:
				return False
		
		else:
			self.d[message] = timestamp 
			return True


# Your Logger object will be instantiated and called as such:
obj = Logger()
print obj.shouldPrintMessage(1,"abc")
print obj.shouldPrintMessage(5,"abc")
print obj.shouldPrintMessage(11,"abc")
print obj.shouldPrintMessage(14,"abc")
print obj.shouldPrintMessage(15,"ac")
print obj.shouldPrintMessage(17,"ac")
