# not really well written code, but interesting problem.
import sys
from copy import deepcopy
filename = sys.argv[1]
from collections import deque
dirs = {"<":(0,-1), ">":(0,1), "^":(-1,0), "v":(1,0)}
def print_grid(grid, x=None, y=None):
	for i,row in enumerate(grid):
		for j,el in enumerate(row):
			if i == x and j == y:
				print("@", end="")
			else:
				print(el, end="")
		print("")
	print("----------------------")

def get_score(grid):
	total = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == "[":
				total += (i*100+j)
	return total

with open(filename) as f:
	data = f.read().split("\n\n")
	grid = [list(x) for x in data[0].splitlines()]
	commands = data[1].strip()
	print(commands)
	bgrid = []
	for row in grid:
		l = []
		for el in row:
			if el == "#":
				l.append("#")
				l.append("#")
			elif el == "O":
				l.append("[")
				l.append("]")
			elif el == ".":
				l.append(".")
				l.append(".")
			elif el == "@":
				l.append("@")
				l.append(".")
		bgrid.append(l)
	grid = bgrid		
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == "@":
				start = (i,j)
				grid[i][j] = "."
	print_grid(grid)
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
		elif nc == "[" or nc == "]":
			to_move = deque()
			to_move.append((x, y,grid[x][y]))
			seen = set()
			while to_move:
				cx, cy, simb= to_move.popleft()
				if simb in "[ ]".split():
					seen.add((cx, cy, simb))
				nx, ny = cx+dx, cy+dy
				if grid[nx][ny] == ".":
					continue
				elif grid[nx][ny] == "#":
					break
				elif grid[nx][ny] == ']':
					if (nx,ny,']') not in seen:
						to_move.append((nx,ny, ']'))
						seen.add((nx,ny,']'))
					if (nx,ny-1,'[') not in seen:
						to_move.append((nx,ny-1, '['))
						seen.add((nx,ny-1,'['))
				elif grid[nx][ny] == '[':
					if (nx,ny,'[') not in seen:
						to_move.append((nx,ny, '['))
						seen.add((nx,ny,'['))
					if (nx,ny+1,']') not in seen:
						to_move.append((nx,ny+1, ']'))
						seen.add((nx,ny+1,']'))
			else:# if no break
				# update grid with stuff in seen
				new_grid = deepcopy(grid)
				for i in range(len(grid)):
					for j in range(len(grid[0])):
						if (i,j,grid[i][j]) in seen:
							new_grid[i][j] = "." # reset old positions
				for i,j,simb in seen:
					new_grid[i+dx][j+dy] = simb
				x,y = x+dx, y+dy
				grid = new_grid
				# print(seen)
		# print(f"Command: {c}")
		# print_grid(grid, x,y)
	print(x,y)
	print_grid(grid)
	print(get_score(grid))
	
			
