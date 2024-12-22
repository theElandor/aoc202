import sys
import time
import math
sys.setrecursionlimit(1000000000)
memo = {}
def cost(a,b):
	return (a*3) + (b*1)

def explore(x,y,a_moves, b_moves, a,b):
	if a > 100 or b > 100:
		return math.inf
	if (x,y,a_moves, b_moves) in memo:
		return memo[(x,y,a_moves, b_moves)]
	if x == 0 and y == 0:
		return cost(a,b)
	if x < 0 or y < 0:
		return math.inf
	dax, day = a_moves
	dbx, dby = b_moves
	r1 = explore(x-dax, y-day, a_moves, b_moves, a+1, b)
	r2 = explore(x-dbx, y-dby, a_moves, b_moves, a, b+1)
	memo[(x,y,a_moves, b_moves)] = min(r1,r2)
	return min(r1,r2)
filename = sys.argv[1]
with open(filename) as f:
	data = f.read().split("\n\n")
	s = {}
	for i,d in enumerate(data):
		s[i] = {"A":[], "B":[]}
		for line in d.splitlines():
			if line.startswith("Button"):
				letter = line.split(":")[0][-1]
				commands = [x.strip() for x in line.split(":")[1].split(",")]
				s[i][letter] = commands
			else:
				prize = [x.strip() for x in line.split(":")[1].split(",")]
				s[i]["prize"] = prize
	t = 0
	for test, sett in s.items():
		print(sett)
		tx, ty = [int(x[2:]) for x in sett["prize"]]
		dax, day = [int(x[2:]) for x in sett["A"]]
		dbx, dby = [int(x[2:]) for x in sett["B"]]
		memo.clear()
		c = explore(tx,ty, (dax, day), (dbx, dby), 0,0)
		if c != math.inf: t+= c
	print(t)
				  
