import sys
filename = sys.argv[1]
dirs = {"<":(0,-1), ">":(0,1), "^":(-1,0), "v":(1,0)}
def print_grid(grid):
	for row in grid:
		for el in row:
			print(el, end="")
		print("")
	print("----------------------")

def find(x,y,dx,dy,grid):
	if grid[x][y] != "O":
		return (x,y)
	return find(x+dx, y+dy, dx, dy, grid)

def get_score(grid):
	total = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == "O":
				total += (i*100+j)
	return total

with open(filename) as f:
	data = f.read().split("\n\n")
	grid = [list(x) for x in data[0].splitlines()]
	commands = data[1].strip()
	print(commands)
	m,n = len(grid), len(grid[0])
	for i in range(m):
		for j in range(n):
			if grid[i][j] == "@":
				grid[i][j] = "."
				start = (i,j)
	x,y = start
	for c in commands:
		if c == "\n":
			continue
		dx, dy = dirs[c]
		nc = grid[x+dx][y+dy]
		if nc == "#":
			pass
		elif nc == ".":
			x,y = x+dx, y+dy
		elif nc == "O":
			ox,oy = find(x+dx,y+dy,dx,dy,grid)
			if grid[ox][oy] == "#":
				continue
			elif grid[ox][oy] == ".":
				grid[ox][oy] = "O"
				grid[x+dx][y+dy] = "."
				x,y = x+dx, y+dy
	print(x,y)
	print_grid(grid)
	print(get_score(grid))
	
			
