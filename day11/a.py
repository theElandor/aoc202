import sys
from collections import deque
filename = sys.argv[1]
with open(filename) as f:
	stones =[int(x) for x in f.read().split()]
	stones = deque(stones)
	blinks = 75
	for b in range(blinks):
		print(b)
		s = len(stones)
		for i in range(s):
			stone = stones.popleft()
			if stone == 0:
				stones.append(1)
			elif len(str(stone))%2 == 0:
				n = len(str(stone))//2
				left = str(stone)[:n]
				right = str(stone)[n:]
				stones.append(int(left))
				stones.append(int(right))
			else:
				stones.append(stone*2024)
	print(len(stones))
		
