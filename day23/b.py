import sys
import networkx as nx
filename = sys.argv[1]
# just find the largest clique!
with open(filename) as f:
	data = f.read().splitlines()
	G = nx.Graph()
	for pair in data:
		n1, n2 = pair.split("-")
		G.add_edge(n1,n2)
	cc = nx.enumerate_all_cliques(G)
	counter = 0
	s = sorted(cc, key=lambda x:len(x), reverse=True)	
	print(",".join(sorted(s[0])))
