import sys
filename = sys.argv[1]
def convert(grid):
	ns = []
	for j in range(len(grid[0])):
		counter = 0
		for i in range(len(grid)):
			if grid[i][j] == "#":
				counter += 1
		ns.append(counter-1)
	return ns
			
with open(filename) as f:
	grids = f.read().split("\n\n")
	locks = []
	keys = []
	for g in grids:
		print(g.splitlines())		
		if g.startswith("#"):
			locks.append(convert(g.splitlines()))
		else:
			keys.append(convert(g.splitlines()))
	print(locks)
	print(keys)
	counter = 0 
	for l in locks:
		for k in keys:
			print(l,k)
			if any([x+y>5 for x,y in zip(l,k)]):pass
			else: counter += 1
	print(counter)
	
