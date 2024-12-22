import sys
import itertools
filename = sys.argv[1]
with open(filename) as f:
	ans =0
	lines = f.read().splitlines()
	for line in lines:
		data = line.split(":")
		target = int(data[0])
		numbers = [int(x) for x in data[1].split()]
		c = itertools.product("*+", repeat=len(numbers)-1)
		for comb in c:			
			i = 0
			current = None
			for x in numbers:
				if not current: current = x
				else:
					current = eval(f"{current}{comb[i]}{x}")
					i += 1
			if current == target:
				print(current, comb)
				ans += current
				break
	print(ans)
				
		
