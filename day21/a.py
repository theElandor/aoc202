import sys
from collections import deque
from heapq import heappop, heappush
from functools import cache
directions = [(0,1), (1,0), (0,-1), (-1,0)]
mapping = {(1,0):"v", (0,1):">", (0,-1):"<", (-1,0):"^"}
numeric = ["7 8 9".split(),"4 5 6".split(),"1 2 3".split(),"_ 0 A".split()]
directional = ["_ ^ A".split(),"< v >".split()]
def get_paths(grid):
	d = {}
	coords = [(x,y) for x in range(len(grid)) for y in range(len(grid[0]))]
	pairs = [(x,y) for x in coords for y in coords]
	for source, dest in pairs:
		ex, ey = dest
		sx,sy = source
		if grid[ex][ey] == "_" or grid[sx][sy] == "_": continue
		Q = [(0,"", sx,sy)]
		best = float("inf")
		while Q:
			distance, pressed, x, y = heappop(Q)
			if distance > best:break
			if distance <= best and grid[x][y] == grid[ex][ey]:
				best = distance
				if (grid[sx][sy], grid[ex][ey]) not in d: d[(grid[sx][sy], grid[ex][ey])] = []
				d[(grid[sx][sy], grid[ex][ey])].append(pressed)
			else:
				for dx, dy in directions:
					if x+dx in range(len(grid)) and y+dy in range(len(grid[0])) and grid[x+dx][y+dy] != "_":
						k = mapping[(dx,dy)]
						heappush(Q, (distance+1, pressed+k, x+dx, y+dy))
	return d
	
d_numeric = get_paths(numeric)
d_directional = get_paths(directional)


def solve(sequence:str, level:int) -> int:	
	if level == 0: return len(sequence)	
	if any([x.isdigit() for x in sequence]):
		sp = d_numeric
	else:
		sp = d_directional
	l = 0
	for x,y in zip("A"+sequence, sequence):
		possibilities = [solve(sub+"A", level-1) for sub in sp[(x,y)]]
		l += min(possibilities)
	return l
		
def print_pad(grid):
	for row in grid:
		for el in row:
			print(el, end="")
		print("")


filename = sys.argv[1]
with open(filename) as f:
	codes = f.read().splitlines()
	depth = 3
	# pre compute all possible shortest paths
	tot = 0
	for c in codes:
		n = solve(c, depth)
		tot += n * int("".join([x for x in c if x.isdigit()]))
	print(tot)


# >>> a = product(["v>", ">v"], ["^<", "<^"])
# >>> list(a)
# [('v>', '^<'), ('v>', '<^'), ('>v', '^<'), ('>v', '<^')]
