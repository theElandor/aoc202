# Some things learned with this puzzle:
# 1) Once you have something that you know it works (p1 of the puzzle)
#    use it to your advantage (to write code with less bugs).
# 2) sometimes turn off your brain and implement the most stupid thing.
#    It will work most of the times.
import sys
filename = sys.argv[1]
from copy import deepcopy
directions = [(-1,0),(0,1),(1,0),(0,-1)]
def ok(i,j, grid):
	if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
		return False
	return True

with open(filename) as f:
	grid = [list(x) for x in f.read().splitlines()]
	for i,row in enumerate(grid):
		for j, col in enumerate(row):
			if col == "^":
				start = (i,j)
	i,j = start
	d = 0
	positions = set()
	loops = 0
	while(True):
		positions.add((i, j))
		di, dj = directions[d]
		if ok(i+di,j+dj,grid):
			if grid[i+di][j+dj] != "#":
				i,j = i+di,j+dj
			else:
				d = (d+1)%len(directions)
		else:
			break
	print(len(positions))
	for x, y in positions:
		if(x,y) == start: continue
		tempgrid = deepcopy(grid)
		tempgrid[x][y] = "#"
		seen = set()
		d = 0
		i,j = start
		while(True):
			if (i,j,d) in seen:
				loops += 1
				break
			else: seen.add((i, j,d))
			di, dj = directions[d]
			if ok(i+di,j+dj,tempgrid):
				if tempgrid[i+di][j+dj] != "#":
					i,j = i+di,j+dj
				else:
					d = (d+1)%len(directions)
			else:
				break		
	print(loops)
