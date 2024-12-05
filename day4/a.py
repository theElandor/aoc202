import sys
filename = sys.argv[1]
directions = [(1,0),(0,1),(-1,0),(0,-1)]
def ok(x,y,grid):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return False
    return True

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
    for order in orders:
        for i,n in enumerate(order):         
            prev = order[:i]
            after = order[i+1:]
            if n not in G:
                if i == len(order)-1:
                    continue
                else:
                    break
            if all([x in G[n] for x in after]):
                continue
            else:
                break
        else:
            good.append(order)
    s = 0
    for g in good:
        s += g[len(g)//2]
    print(s)


    
    
