import sys
filename = sys.argv[1]
def ok(i,j, grid):
	if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
		return False
	return True

# def print_path(grid, s):
# 	for i,row in enumerate(grid):
# 		for j, col in enumerate(row):
# 			if (i,j) in s:
# 				print("X", end="")
# 			else:
# 				print(".", end="")
# 		print("")

with open(filename) as f:
	grid = [list(x) for x in f.read().splitlines()]
	print(grid)
	for i,row in enumerate(grid):
		for j, col in enumerate(row):
			if col == "^":
				start = (i,j)
	current = start
	i,j = current
	directions = [(-1,0),(0,1),(1,0),(0,-1)]
	d = 0
	total = 0
	positions = set()
	loops = 0
	while(True):
		positions.add((i, j))
		i,j = current
		di, dj = directions[d%len(directions)]
		if ok(i+di,j+dj,grid):
			if  grid[i+di][j+dj] != "#":
				current = i+di,j+dj				
				total += 1
			else:
				d += 1
		else:
			break
#	print_path(grid, positions)
	print(len(positions)+1)
	print(loops)
