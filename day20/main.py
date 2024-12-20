import sys
from copy import deepcopy
import math
from collections import deque
directions = [(1,0), (0,1), (0,-1), (-1,0)]
filename = sys.argv[1]
# spent a ton of time on a more difficult approach.
# Should think more before trying to solve the problem in a fancy way.
# There is always a easier way to do stuff.
def bfs(start, end, grid):
	x,y = start
	m = len(grid)
	n = len(grid[0])
	dists = [[math.inf]*n for _ in range(m)]
	dists[x][y] = 0
	Q = deque([(0, x, y)])
	seen = set()
	seen.add(start)
	while Q:
		distance, x,y = Q.popleft()
		if (x,y) == end:
			return dists
		for dx, dy in directions:
			if x+dx in range(m) and y+dy in range(n) and grid[x+dx][y+dy] != "#" and (x+dx, y+dy) not in seen:
				Q.append((distance+1, x+dx, y+dy))
				seen.add((x+dx, y+dy))
				dists[x+dx][y+dy] = distance+1
	return dists

# part 1
# def search(start, end, grid, dists):
# 	m = len(grid)
# 	n = len(grid[0])
# 	saved = []
# 	for i in range(m):
# 		for j in range(n):			
# 			current = dists[i][j]
# 			print(current)
# 			if grid[i][j] == "#" or current == math.inf: continue
# 			for di, dj in directions:
# 				ni,nj = i+(2*di), j+(2*dj)
# 				if ni in range(m) and nj in range(n) and grid[ni][nj] != "#" and 2 + current < dists[ni][nj]:
# 					saved.append(dists[ni][nj] - (2+current))
# 	return saved


#part2
def search(start, end, grid, dists):
	m = len(grid)
	n = len(grid[0])
	saved = []
	for i in range(m):
		for j in range(n):
			print(i,j)
			current = dists[i][j]
			if grid[i][j] == "#" or current == math.inf: continue
			for di in range(-20, 21):
				for dj in range(-20,21):
					ni,nj = i+di, j+dj
					if ni in range(m) and nj in range(n) and grid[ni][nj] != "#" and (abs(di)+abs(dj)) <= 20 and (abs(di)+abs(dj)) + current < dists[ni][nj]:
						saved.append(dists[ni][nj] - ((abs(di)+abs(dj))+current))
			# for di, dj in directions:
			# 	ni,nj = i+(2*di), j+(2*dj)
			# 	if ni in range(m) and nj in range(n) and grid[ni][nj] != "#" and 2 + current < dists[ni][nj]:			
			# 		saved.append(dists[ni][nj] - (2+current))
	return saved


with open(filename) as f:
	grid = [list(x) for x in f.read().splitlines()]
	m = len(grid)
	n = len(grid[0])
	for i in range(m):
		for j in range(n):
			if grid[i][j] == "S":
				start = (i,j)
			elif grid[i][j] == "E":
				end = (i,j)
	x,y = start
	xe,ye = end
	dists = bfs(start, end, grid)
	sp = dists[xe][ye]
	print(f"Shortest path {sp}")
	print(dists)
	ans = search(start, end, grid, dists)
#	print(sorted(ans))
	print(len([x for x in ans if x >= 100]))
#	print({x:ans.count(x) for x in ans})
