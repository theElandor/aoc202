import sys
from heapq import heappush,heappop
directions = [(1,0), (0,1), (0,-1), (-1,0)]
filename = sys.argv[1]
def print_grid(m,n, corr):
	for i in range(m):
		for j in range(n):
			if (j,i) in corr:
				print("#", end="")
			else:
				print(".", end="")
		print("")
		
with open(filename) as f:
	coords = [[int(y) for y in x.split(",")] for x in f.read().splitlines()]
	starting = coords[:1024]
	check = coords[1024:]
	x,y = 0,0
	m,n = 71,71
	corr = set()
	for c in starting:
		corr.add(tuple(c))
	Q = [(0,x,y)]
	seen = set((x,y))
	print_grid(m,n,corr)
	while Q:
		print(Q)
		distance, x,y = heappop(Q)
		if (x,y) == (m-1, n-1):
			print(distance)
			break
		for dx, dy in directions:
			if x+dx in range(m) and y+dy in range(n) and (y+dy, x+dx) not in corr and (x+dx, y+dy) not in seen:
				heappush(Q, (distance+1, x+dx, y+dy))
				seen.add((x+dx, y+dy))
	
