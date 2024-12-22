import sys
from collections import deque
from heapq import heappop, heappush
from copy import deepcopy
directions = [(0,1), (1,0), (0,-1), (-1,0)]
mapping = {(1,0):"v", (0,1):">", (0,-1):"<", (-1,0):"^"}
numeric = ["7 8 9".split(),"4 5 6".split(),"1 2 3".split(),"_ 0 A".split()]
directional = ["_ ^ A".split(),"< v >".split()]
# def dist(grid, start,end):
# 	x,y = start	
# 	Q = deque([(0,x,y,[],set())])
# 	m = len(grid)
# 	n = len(grid[0])
# 	res = []
# 	best = None
# 	while Q:
# 		distance, x,y, moves, seen = Q.popleft()
# 		if best != None and distance > best: continue
# 		if (x,y) == end:
# 			res.append(moves)
# 			best = distance
# 		else:
# 			for dx,dy in directions:
# 				if x+dx in range(m) and y+dy in range(n) and (x+dx, y+dy) not in seen and grid[x+dx][y+dy] != "_":
# 					newmoves = deepcopy(moves)
# 					newseen = deepcopy(seen)
# 					newmoves.append(mapping[(dx,dy)])
# 					newseen.add((x+dx, y+dy))
# 					Q.append((distance+1,x+dx,y+dy, newmoves, newseen))
# 	# keep path with most cons. numb of moves
# 	stuff = []
# 	print(res)
# 	for path in res:
# 		counter = 0
# 		for i in range(len(path)-1):
# 			if path[i] == path[i+1]:
# 				counter += 1
# 		stuff.append((counter, path))
# 	return (sorted(stuff, reverse=True)[0][1])
#	return sorted(stuff, reverse=True)[0][1]

def print_pad(grid):
	for row in grid:
		for el in row:
			print(el, end="")
		print("")

def find_k(grid, target):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == target:
				return (i,j)
	return -1

def valid(current, target):
	for i in range(len(current)):
		if current[i] != target[i]:
			return False
	return True

def transform(code, grid):
	print(code)
	lc = len(code)
	rx,ry = find_k(grid, "A")
	Q = []
	heappush(Q, (0,rx,ry,[],0))
	m = len(grid)
	n = len(grid[0])
	best = None
	ans = []
	while Q:
		distance, x, y, kp, bs = heappop(Q)
		print(distance, x, y, kp, bs)
		if best != None and distance > best:
			continue
		if lc == bs:
			if best == None:
				best = distance
				ans.append(kp)
			elif best == distance:
				ans.append(kp)
			continue
		# press dir key
		for dx, dy in directions:
			if best != None and distance+1 > best: continue
			if x+dx in range(m) and y+dy in range(n):				
				newkp = deepcopy(kp)
				newkp.append(mapping[(dx,dy)])
				heappush(Q,(distance+1, x+dx, y+dy, newkp, bs))
			# try to press A if did not press A before
		if len(kp) != 0 and kp[-1] == "A": continue
		if code[bs] != grid[x][y]: continue
		newkp = deepcopy(kp)
		newkp.append("A")
		heappush(Q, (distance, x,y,newkp, bs+1))
	stuff = []
	for path in ans:
		counter = 0
		for i in range(len(path)-1):
			if path[i] == path[i+1]:
				counter += 1
		stuff.append((counter, path))
	return (sorted(stuff, reverse=True)[0][1])
	

filename = sys.argv[1]
with open(filename) as f:
	test = transform(list("029A"), numeric)
	test = transform(test, directional)
	print(test)
	# solution = {}
	# res = 0
	# for code in ["A"+c for c in codes]:
	# 	s = process_sequence(code, numeric)
	# 	print(s)
	# for code in ["A"+c for c in codes]:
	# 	sequence = solution[code]
	# 	new_sequence = process_sequence("A"+sequence, directional)
	# 	print(new_sequence)
	# 	break
		# new_new_sequence = process_sequence("A"+new_sequence, directional)
		# print(f"finlen:{len(new_new_sequence)} {code} \n {sequence} \n {new_sequence} \n {new_new_sequence}")
		# res += len(new_new_sequence) * int("".join([c for c in code if c.isdigit()]))
	
	
