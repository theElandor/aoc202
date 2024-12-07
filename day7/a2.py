import sys
import itertools
sys.setrecursionlimit(1000000)
filename = sys.argv[1]
def solve(target, numbers, index, current):
	if current == target:
		if index == len(numbers):
			return True
	if index >= len(numbers):
		return False
	n = numbers[index]
	return solve(target, numbers, index+1, current+n) or solve(target, numbers, index+1, current*n)

		
	
with open(filename) as f:
	ans =0
	lines = f.read().splitlines()	
	for line in lines:
		target, numbers = line.split(":")
		ns = [int(x) for x in numbers.split()]
		print(target, ns)
		if solve(int(target), ns, 1, ns[0]):
			ans += int(target)
	print(ans)
