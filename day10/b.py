import sys
directions = [(1,0),(0,1),(0,-1),(-1,0)]
ends = []
def ok(grid, i, j):
	if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
		return False
	if grid[i][j] == ".":
		return False
	return True
	
def check(grid, i, j):
	if grid[i][j] == 9:
		ends.append((i,j))
	current = grid[i][j]
	for di, dj in directions:
		if ok(grid, i+di, j+dj) and grid[i+di][j+dj] == current+1 and (i+di,j+dj):
			check(grid, i+di, j+dj)
			
				
filename = sys.argv[1]
with open(filename) as f:
	grid = [[int(x) for x in list(line)] for line in f.read().splitlines()]
	total = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 0:
				check(grid, i,j)
				total += len(ends)
				ends.clear()
	print(total)
