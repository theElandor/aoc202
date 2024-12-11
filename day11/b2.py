# could have been faster with a recursive solution
# with memoization
import sys
import time
sys.setrecursionlimit(100000000)
from collections import deque
filename = sys.argv[1]
memo = {}
def solve(n, time):
	if (n,time) in memo:
		return memo[(n,time)]
	if time == 0:		
		res = 1
	elif n == 0:
		res=solve(1, time-1)
	elif len(str(n))%2 == 0:
		r = len(str(n))//2
		left = int(str(n)[:r])
		right = int(str(n)[r:])
		res = solve(right, time-1) + solve(left, time-1)
	else:
		res = solve(n*2024, time-1)
	memo[(n,time)] = res
	return res
with open(filename) as f:
	stones =[int(x) for x in f.read().split()]
	total = 0
	blinks = 75
	for s in stones:
		total += solve(s,blinks)
	print(total)
