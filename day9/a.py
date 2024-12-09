import sys
filename = sys.argv[1]
with open(filename) as f:
	nums = [int(x) for x in list(f.read().strip())]
	id = 0
	mem = []
	for i,n in enumerate(nums):
		if i%2 != 0:
			mem += ["." for _ in range(n)]
		else:
			mem += [str(id) for _ in range(n)]
			id += 1	
	r = len(mem)-1
	n = len(mem)
	l = 0
	# mem[l],mem[r] = mem[r], mem[l]
	while l < r:
		if mem[l] == "." and mem[r] == ".":
			r -= 1
		elif mem[l] == "." and mem[r] != ".":
			mem[l],mem[r] = mem[r], mem[l]
			l += 1
			r -= 1
		elif mem[l] != "." and mem[r] != ".":
			l += 1
		elif mem[l] != "." and mem[r] == ".":
			l += 1
			r -= 1
		else:
			raise Exception
	ans = sum([i *int(n) for i, n in enumerate(mem) if n != "."])
	print("".join(mem))
	print(ans)
		
		
