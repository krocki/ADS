# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-12 20:22:32
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-12 21:16:30

def find(nodes, val):

	l = [i for i in nodes if i.val == val]
	if l: return l[0]
	else: return None

# TODO: improve
def traverse(node):

	print "{" + str([traverse(i) for i in node.children]) + "}"

	return node.val

def lookup(node, string):
	
	if len(string) == 0:
		return node
	else:
		x = string[0]
		n = find(node.children, x)
		if n == None: return None
		else: 
			if len(string) == 1: 
				traverse(node)
				return n
			else: return lookup(n, string[1:])

def insert(node, string):

	if len(string) == 0: x = '*'
	else: x = string[0]

	n = find(node.children, x)

	if n == None:
		n = Node(x)
		node.children.append(n)

	if len(string) > 0:
		xs = string[1:]
		insert(n, xs)
	

class Node:

	children = []
	val = None

	def __init__(self, val):
		self.val = val
		self.children = []

root = Node("#")
insert(root, "car")
insert(root, "cat")
insert(root, "cart")
insert(root, "cars")

traverse(root)

print "looking up... ca"
lookup(root, "ca")
