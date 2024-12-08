import sys
import math
directions = [(0,1),(1,0),(0,-1),(-1,0), (-1,-1),(1,1),(-1,1), (1,-1)]
from collections import deque
# m = (yb-ya)/(xb-xa)

def ok(i,j,grid):
    if i >= len(grid) or i < 0 or j < 0 or j >= len(grid[0]):
        return False
    return True

def coeff(a,b): # line gradient function
	x1, y1 = a
	x2, y2 = b
	if x1 == x2:
		return math.inf
	return (y1-y2)/(x1-x2)

def bfs(i,j,grid, signals): # bfs to compute distances
	# as the grid has no obstacles, we could have used
	# just manhattan distance :(
	Q = deque()
	Q.append((0,i,j))
	seen = set((i,j))
	source = grid[i][j]
	while Q:
		d,r,c = Q.popleft()
		for dr,dc in directions:
			if ok(r+dr, c+dc, grid) and (r+dr, c+dc) not in seen:
				Q.append((d+1, r+dr, c+dc))
				seen.add((r+dr,c+dc))
				# distance, coeff
				if source not in signals[(r+dr,c+dc)]:
					signals[(r+dr,c+dc)][source] = [(d+1, coeff((i,j),(r+dr, c+dc)))]
				else:
					signals[(r+dr,c+dc)][source].append((d+1, coeff((i,j),(r+dr, c+dc))))
				
def print_grid(grid): # helper function to print grid
	for row in grid:
		for col in row:
			print(col, end="")
		print("")
	
			
filename = sys.argv[1]
with open(filename) as f:
	ans = 0
	grid = [list(x) for x in f.read().splitlines()]
	signals = {}
	# init signals
	for i, row in enumerate(grid):
		for j, el in enumerate(row):
			signals[(i,j)] = {}	
	for i, row in enumerate(grid):
		for j, el in enumerate(row):
			if grid[i][j] != ".":
				bfs(i,j,grid, signals)
	seen = set()
	for i,row in enumerate(grid):
		for j,el in enumerate(row):
			if el != ".":
				ans+=1
				grid[i][j] = "#"
				
	for key, val in signals.items():
		i,j = key
		for k,v in val.items():
			print(f"[{i},{j}]",k,v)
			for k,(d1,c1) in enumerate(v):
				for d2,c2 in v[k+1:]:
					if c1 == c2:
						print(i,j)
						if grid[i][j] != "#":
							grid[i][j] = "#"
							ans += 1

	print_grid(grid)
	print(ans)
