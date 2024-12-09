# can't debug this s**t
# taking 10 extra minutes to write a nicer logic is better
# then taking 1 hour trying to debug a cluttered stupid logic
import sys
filename = sys.argv[1]
def find_space(mem, r):
	ref = mem[r]
	els = 0
	while mem[r] == ref:
		r-=1
		els += 1
#	print(f"found {els} elements {ref}")
	# must find els contig spaces
	l = 0
	space = 0
	last = None
	while l < r:
		if mem[l] == ".":
			if not last: last = l
			space+=1
			if space == els: return last, els
		else:
			space = 0
			last = None
		l += 1
	return -1,-1
	
with open(filename) as f:
	nums = [int(x) for x in list(f.read().strip())]
	id = 0
	mem = []
	for i,n in enumerate(nums):
		if i%2 != 0:
			mem += ["." for _ in range(n)]
		else:
			mem += [id for _ in range(n)]
			id += 1
	r = len(mem)-1
	moved = set()
	while r >= 0:
		# print("".join(mem))
		if mem[r] == ".":
			r -= 1
		else:
			ref = mem[r]
			if ref in moved:
				r-=1
				continue
			index,els = find_space(mem, r)
#			print(f"found {els} spaces starting at {index}")
			if index == -1:
				# skip block				
				while mem[r] == ref:
					r -= 1
#				print(f"no space found for block {ref}, r is {r}")
			else:
				# copy
				mem[index:index+els] = [ref]*els
				# [r-els+1, r+1]
#				print(f"copied {mem[r-els+1:r+1]}, now r is {r-els-1}")
				mem[r-els+1:r+1] = ["."]*els
				moved.add(ref)				
				r = r-els
	ans = sum([i *int(n) for i, n in enumerate(mem) if n != "."])
	print(ans)
	if filename == "test.txt":
		print([i *int(n) for i, n in enumerate(mem) if n != "."])
		print("".join([str(x) for x in mem]))
# 6488291456470 c
# 6488291823733
