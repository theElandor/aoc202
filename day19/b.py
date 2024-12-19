import sys
import time
from copy import deepcopy
filename = sys.argv[1]
memo = {}
def solve(pattern, t):
	if pattern in memo: return memo[pattern]
	ans = 0
	if pattern == "":
		return 1
	for c in t:
		if pattern.startswith(c):
			ans += solve(pattern[len(c):], t)
	memo[pattern] = ans
	return ans
	
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
	print(end-start)
	



	# a b c d d e f a b c a b c a b c
