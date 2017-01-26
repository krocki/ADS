# -*- coding: utf-8 -*-
# @Author: Kamil M Rocki
# @Date:   2017-01-25 15:59:49
# @Last Modified by:   Kamil M Rocki
# @Last Modified time: 2017-01-25 16:26:18

def islandPerimeter(grid):
	"""
	:type grid: List[List[int]]
	:rtype: int
	"""

	perimeter = 0

	for i,row in enumerate(grid):
		for j, e in enumerate(row):
			if e: 
				perimeter += 4
				if i < len(grid)-1 and grid[i+1][j]: perimeter -= 2
				if j < len(grid[i])-1 and grid[i][j+1]: perimeter -= 2

	return perimeter

i = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]

print islandPerimeter(i)