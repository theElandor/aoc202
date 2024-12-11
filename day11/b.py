# could have been faster with a recursive solution
# with memoization
import sys
import time
from collections import deque
filename = sys.argv[1]
with open(filename) as f:
	stones =[int(x) for x in f.read().split()]
	sd = {s:stones.count(s) for s in stones}	
	blinks = 75
	for b in range(blinks):
		temp = {}
		for k, val in sd.items():
			if k == 0:
				if 1 in temp:
					temp[1] += val
				else:
					temp[1] = val
			elif len(str(k))%2 == 0:
				n = len(str(k))//2
				left = int(str(k)[:n])
				right = int(str(k)[n:])
				if right in temp: temp[right] += val
				else: temp[right] = val
				if left in temp: temp[left] += val
				else: temp[left] = val
			else:
				if k*2024 in temp:
					temp[k*2024] += val
				else:
					temp[k*2024] = val
		sd = temp
	print(sum([val for key,val in sd.items()]))
