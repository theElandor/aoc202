# had to lookup some hits for this one as I've never seen
# a similar problem before. Really interesting anyway.
# The key insight is that we only care about the last 3 digits of A,
# since the first thing we do is setting B as a % 8 (means setting B as the
# last 3 digits of A). This means that at each iteration we can just do cand << 3
# to save the last 3 digits and then try to add numbers from 1 to 7 to actually try
# if it gives us the right solution.
import sys
filename = sys.argv[1]
def combo(x,A,B,C):
	if 0 <= x <= 3:
		return x
	if x == 4:
		return A
	if x == 5:
		return B
	if x == 6:
		return C
	if x == 7:
		raise Exception

def run(program, A):
	# assuming B and C always start at 0
	B = 0
	C = 0
	out = []
	i = 0
	while i < len(program):
		opcode = program[i]
		x = program[i+1]
		if opcode == 0:
			A = int(A/(2**combo(x, A,B,C)))
			i += 2
		elif opcode == 1:
			B = B ^ x
			i += 2
		elif opcode == 2:
			B = combo(x, A,B,C) % 8
			i += 2
		elif opcode == 3:
			if A == 0:
				i+=2
				continue
			i = x
		elif opcode == 4:
			B = B ^ C
			i += 2
		elif opcode == 5:
			out.append(combo(x,A,B,C) % 8)
			i+=2
		elif opcode == 6:			
			B = int(A/(2**combo(x, A,B,C)))
			i += 2
		elif opcode == 7:
			C = int(A/(2**combo(x, A,B,C)))
			i += 2
	return out

from collections import deque	
with open(filename) as f:
	data = f.read().split("\n\n")
	program = [int(x) for x in data[1][9:].split(",")]
	cands = deque([0])
	shifts = 0
	for target in program[::-1]:
		print(f"target: {target}")
		new_cands = []
		while cands:
			current =(cands.popleft())<<3
			for i in range(8):
				if run(program, current+i)[0] == target:
					new_cands.append(current+i)
		print(new_cands)
		cands = deque(new_cands)
	print(min(cands))
	
	
	

