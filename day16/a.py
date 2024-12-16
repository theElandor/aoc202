import sys
from heapq import heappop, heappush
directions = [(0,1),(1,0),(0,-1),(-1,0)]
filename = sys.argv[1]
with open(filename) as f:
	grid = [list(x) for x in f.read().splitlines()]
	m,n = len(grid), len(grid[0])
	for i in range(m):
		for j in range(n):
			if grid[i][j] == "S":
				start = (0,0,i,j)
			if grid[i][j] == "E":
				end = (i,j)
	Q = []
	Q.append(start)
	print(end)
	print(start)
	seen = set()
	while Q:	
		distance,facing, i,j = heappop(Q)
		seen.add((facing, i, j))
		print(distance, facing, i, j)
		if (i,j) == end:
			print(distance)
			break
		if ((facing+1)%4,i,j) not in seen:
			heappush(Q, (distance+1000, ((facing+1)%4),i,j))
		if ((facing-1)%4, i,j) not in seen:
			heappush(Q,(distance+1000, ((facing-1)%4),i,j))
		di, dj = directions[facing]
		if i+di in range(m) and j+dj in range(n) and grid[i+di][j+dj] != "#" and (facing, i+di,j+dj) not in seen:
			heappush(Q,(distance+1, facing, i+di, j+dj))
		
		
