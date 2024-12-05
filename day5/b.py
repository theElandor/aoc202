import sys
from collections import deque
from copy import deepcopy
# took me like 30 mins to realize that 
# I was using G instead of g in the topological sort function.
# 6 am hits right in the spot.

filename = sys.argv[1]
def topo(G, ordering):
    S = deepcopy(G)    
    g = {x:v for x,v in S.items() if x in ordering}    
    source = []
    for k,_ in g.items():
        if all([k not in v for _,v in g.items()]):
            source.append(k)
    L = []
    S = deque(source)
    while len(S) != 0:
        n = S.popleft()
        if n in ordering:
            L.append(n)
        if n not in g:
            continue
        while len(g[n]) != 0:
            m = g[n].pop()
            if all(m not in v for k,v in g.items()):
                S.append(m)
    return L
      
with open(filename) as f:
    data = f.read().split("\n\n")
    b1 = [x.split("|") for x in data[0].splitlines()]
    b2 = [x.split(",") for x in data[1].splitlines()]
    rules = [(int(x), int(y)) for x,y in b1]
    orders = [[int(x) for x in y] for y in b2]    
    G = {}
    for u,v in b1:
        u,v = int(u), int(v)
        if u in G:
            G[u].append(v)
        else:
            G[u] = [v]
    sources = [key for key,val in G.items() if len(val) == 0]
    nodes = set(G.keys())
    good = []
    bad = []
    for order in orders:
        for i,n in enumerate(order):         
            prev = order[:i]
            after = order[i+1:]
            if n not in G:
                if i == len(order)-1:
                    continue
                else:
                    bad.append(order)
                    break
            if all([x in G[n] for x in after]):
                continue
            else:
                bad.append(order)
                break
    s = 0
    for b in bad:
        t = topo(G,b)
        print(f"{b} --> {t}")
        s += t[len(t)//2]
    print(s)
                 
        