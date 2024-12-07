import sys
import itertools
sys.setrecursionlimit(1000000)
# a more elegant recursive solution
filename = sys.argv[1]
def solve(target, numbers, index, current):
	if current == target:
		if index == len(numbers):
			return True
	if index >= len(numbers):
		return False
	n = numbers[index]
	add = solve(target, numbers, index+1, current+n)
	mul = solve(target, numbers, index+1, current*n)
	concat = solve(target, numbers, index+1, eval(str(current)+str(n)))
	return  add or mul or concat

		
	
with open(filename) as f:
	ans =0
	lines = f.read().splitlines()	
	for line in lines:
		target, numbers = line.split(":")
		ns = [int(x) for x in numbers.split()]
		if solve(int(target), ns, 1, ns[0]):
			print(target)
			ans += int(target)
	print(ans)
