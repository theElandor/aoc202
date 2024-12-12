import sys
g = [0,0] # area, perimeter
directions = [(1,0),(0,1),(-1,0),(0,-1)]
def ok(i,j,grid):
	if i in range(len(grid)) and j in range(len(grid[0])):
		return True
	return False

def dfs(i, j, grid, seen):
	g[0] += 1
	freedoms = 0
	current = grid[i][j]
	seen.add((i,j))
	for di,dj in directions:
		if not ok(i+di, j+dj, grid):
			freedoms += 1
		elif grid[i+di][j+dj] != current:
			freedoms += 1
		else:
			if (i+di, j+dj) not in seen:
				dfs(i+di,j+dj, grid, seen)
	g[1] += freedoms
filename = sys.argv[1]
with open(filename) as f:
	grid = [list(x) for x in f.read().splitlines()]
	seen = set()
	total = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if (i,j) not in seen:
				dfs(i,j,grid, seen)
				area, per = g
				total += (area*per)
				g = [0,0]
	print(total)
