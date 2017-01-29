# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-01-26 11:21:21
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-01-26 11:37:14


def countBattleships(board):
	"""
	:type board: List[List[str]]
	:rtype: int
	"""
	count = 0

	x = 0
	y = 0

	for x in range(0,len(board)):
		for y in range(0,len(board[x])):
			
			if board[x][y] == 'X' and (y == 0 or board[x][y-1] == '.') and (x == 0 or board[x-1][y] == '.'):
				count += 1

	return count

board = [['X','.','.','X'], ['.','.','.','X'], ['.','.','.','X']]

print countBattleships(board)