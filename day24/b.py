import sys
import graphviz
filename = sys.argv[1]
# "just" print with graphviz the adder dependency tree
# and look for errors in connections.
def make_op(l,o,r):
	assert o in "AND OR XOR".split()
	if o == "AND":
		return l and r
	if o == "OR":
		return l or r
	if o == "XOR":
		return l ^ r

def get_number(mem, gt):
	gates = sorted([k for k, v in mem.items() if k.startswith(gt)], key=lambda x:int(x[1:]), reverse=True)
	binary = "".join([str(mem[x]) for x in gates])
	return (int(binary, 2))

with open(filename) as f:
	data = f.read().split("\n\n")
	mem = {x.split(":")[0]:int(x.split(":")[1]) for x in data[0].splitlines()}
	x = get_number(mem,"x")
	y = get_number(mem,"y")
	print(x,y)
	ops = [(x.split("->")[0].split(" ")[:-1],x.split(" -> ")[1]) for x in data[1].splitlines()]
	# made = set()
	# while len(made) != len(ops):
	# 	for i,((l,o,r), og) in enumerate(ops):
	# 		if l in mem and r in mem and i not in made:
	# 			mem[og] = make_op(mem[l],o,mem[r])
	# 			made.add(i)
	# print(get_number(mem, "z"))
	print(ops)
	print(mem)
	# g = graphviz.Digraph('G', filename="test.gv")
	# for (l,o,r), og in ops:
	# 	g.edge(l,og, label=o)
	# 	g.edge(r,og, label=o)
	# g.view()

	
# manual inspect of the graph -> gdd z05 cwt z09 css jmv pqt z37
# css cwt gdd jmv pqt z05 z09 z37
