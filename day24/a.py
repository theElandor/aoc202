import sys
filename = sys.argv[1]
def make_op(l,o,r):
	assert o in "AND OR XOR".split()
	if o == "AND":
		return l and r
	if o == "OR":
		return l or r
	if o == "XOR":
		return l ^ r
	
with open(filename) as f:
	data = f.read().split("\n\n")
	mem = {x.split(":")[0]:int(x.split(":")[1]) for x in data[0].splitlines()}
	ops = [(x.split("->")[0].split(" ")[:-1],x.split(" -> ")[1]) for x in data[1].splitlines()]
	made = set()
	while len(made) != len(ops):
		for i,((l,o,r), og) in enumerate(ops):
			if l in mem and r in mem and i not in made:
				mem[og] = make_op(mem[l],o,mem[r])
				made.add(i)
	z_gates = sorted([k for k, v in mem.items() if k.startswith("z")], key=lambda x:int(x[1:]), reverse=True)
	print(z_gates)
	binary = "".join([str(mem[x]) for x in z_gates])
	print(int(binary, 2))
