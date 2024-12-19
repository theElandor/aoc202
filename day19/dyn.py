import sys
import time
from copy import deepcopy
filename = sys.argv[1]
# sort of bottom up dp solution
mem = {}
def solve(target:str,t:list):
	# at each step, I can take all things in t
	# abcd
	# d cd bcd ...
	current = ""
	for i in range(len(target)-1, -1, -1):
		current = target[i] + current
		temp = 0
		for p in t:
			if current.startswith(p):
				prev = current[len(p):]
				if len(prev) == 0: temp+=1
				else: temp+=mem[prev]
		mem[current] = temp
	return mem[target]
				
	
with open(filename) as f:
	start = time.time()
	data = f.read().split("\n\n")
	t = data[0].split(", ")
	patterns = data[1].splitlines()
	total = 0
	for p in patterns:
		ans = solve(p, t)
		total += ans
	print(total)
	end = time.time()
	print(end - start)
	
