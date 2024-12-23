import sys
import networkx as nx
filename = sys.argv[1]
# we just need to find the cliques (complete subgrpahs with 3 nodes)
with open(filename) as f:
	data = f.read().splitlines()
	G = nx.Graph()
	for pair in data:
		n1, n2 = pair.split("-")
		G.add_edge(n1,n2)
	cc = nx.enumerate_all_cliques(G)
	counter = 0
	for clique in cc:
		if len(clique) == 3:
			if any([node[0]=="t" in list(node) for node in clique]):
				counter += 1				
	print(counter)
