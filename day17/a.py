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

with open(filename) as f:
	data = f.read().split("\n\n")
	A, B, C = [int(x[12:]) for x in data[0].splitlines()]
	program = [int(x) for x in data[1][9:].split(",")]
	maxstuff = 100000000
	for A in range(maxstuff):
		if A % 10000 == 0: print(A)
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
		print(out)
		if out == program:
			break

