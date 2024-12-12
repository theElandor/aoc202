# very cool and hard problem.
# we mark stuff outside the perimeter with half-coordinates
# to avoid "corner problems". Then we pop elements from
# the marked set and run a dfs along vertical and horizontal axis.
# We also need to keep track of direction to avoid problems with overlapping fences.

import sys
import random
g = [0,0] # area, perimeter
directions = [(1,0),(0,1),(-1,0),(0,-1)]
temp = set()
diags = [(-.5,-.5), (.5,.5), (-.5,.5), (.5,-.5),(1,0),(0,1),(-1,0),(0,-1)]
bseen = set()
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
			marked.add((i+(di/2),j+(dj/2)))
			sides[(i+(di/2),j+(dj/2))] = (di,dj)
		elif grid[i+di][j+dj] != current:
			freedoms += 1
			marked.add((i+(di/2),j+(dj/2)))
			sides[(i+(di/2),j+(dj/2))] = (di,dj)
		else:
			if (i+di, j+dj) not in seen:
				dfs(i+di,j+dj, grid, seen)
	g[1] += freedoms

def lines(i,j,marked):
	current_side = sides[(i,j)]
	for di,dj in directions:
		if (i+(di/2)).is_integer() and (j+(dj/2)).is_integer():
			continue # try another direction
		if (i+di,j+dj) in marked and sides[(i+di, j+dj)] == current_side:
			marked.remove((i+di, j+dj))
			lines(i+di, j+dj, marked)
			

filename = sys.argv[1]	
with open(filename) as f:
	grid = [list(x) for x in f.read().splitlines()]
	seen = set()
	total = 0
	marked = set()
	sides = {}
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			current = grid[i][j]
			if (i,j) not in seen:				
				dfs(i,j,grid, seen)
				area, per = g
				fences = 0
#				print(marked)
				while marked:					
					si,sj = random.sample(marked, 1)[0]
					#print(si,sj)
					marked.remove((si,sj))
					lines(si,sj,marked)
					fences += 1
				print(f"{current}-->{area}, {fences}")
				total += (fences)*area
				g = [0,0]
			marked.clear()
			sides.clear()
			bseen.clear()
	print(total)
