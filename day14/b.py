import sys
filename = sys.argv[1]
seconds = int(sys.argv[2])
def print_grid(grid):
	for row in grid:
		for el in row:
			if el != 0:
				print(el, end="")
			else:
				print(".", end="")
		print("")
with open(filename) as f:
	lines = f.read().splitlines()
	robots = []
	for l in lines:
		r = {}
		data = l.split(" ")
		r["p"] = [int(x) for x in data[0][2:].split(",")]
		r["v"] = [int(x) for x in data[1][2:].split(",")]
		robots.append(r)
	w,h = 101,103
	#w,h = 11,7
	for s in range(1,seconds+1):
		seen = set()
		grid = [[0 for _ in range(w)] for _ in range(h)]	
		for r in robots:
			cc, cr = r["p"]
			dc, dr = r["v"]
			fc = (cc+(s*dc))%w
			fr = (cr+(s*dr))%h
			grid[fr][fc] += 1
			seen.add((fr,fc))
		if len(seen) == len(robots):
			print(s)
			print_grid(grid)
#		print("------------")
#		print_grid(grid)		
