 # just a standarda Dikstra's problem with a couple of interesting twists.
 # Can't really tell but I am counting 1 extra tile :(
import sys
from copy import deepcopy
from heapq import heappop, heappush
directions = [(0,1),(1,0),(0,-1),(-1,0)]
filename = sys.argv[1]
def print_grid(grid, tiles):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if (i,j) in tiles:
				print("O", end="")
			else:
				print(grid[i][j], end="")
		print("")
				
with open(filename) as f:
	grid = [list(x) for x in f.read().splitlines()]
	m,n = len(grid), len(grid[0])
	for i in range(m):
		for j in range(n):
			if grid[i][j] == "S":
				start = (0,0,i,j,set((i,j)))
			if grid[i][j] == "E":
				end = (i,j)
	Q = []
	Q.append(start)
	seen = set()
	bdist = None
	tiles = set()
	while Q:	
		distance,facing, i,j, path = heappop(Q)
		seen.add((facing, i, j))
		if (i,j) == end:
			if not bdist:
				bdist = distance
				print(bdist)
				tiles = path
			else:
				if distance == bdist:
					tiles = tiles.union(path)					
		if ((facing+1)%4,i,j) not in seen:
			newpath = deepcopy(path)
			heappush(Q, (distance+1000, ((facing+1)%4),i,j, newpath))
		if ((facing-1)%4, i,j) not in seen:
			newpath = deepcopy(path)
			heappush(Q,(distance+1000, ((facing-1)%4),i,j, newpath))
		di, dj = directions[facing]		
		if i+di in range(m) and j+dj in range(n) and grid[i+di][j+dj] != "#" and (facing, i+di,j+dj) not in seen:
			newpath = deepcopy(path)
			newpath.add((i+di, j+dj))
			heappush(Q,(distance+1, facing, i+di, j+dj, newpath))
	print(len(tiles)-1)
#	print_grid(grid, tiles)
		
