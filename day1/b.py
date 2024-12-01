with open("input.txt") as f:
    grid = f.read().splitlines()
    items = [[int(y) for y in x.split("   ")] for x in grid]
    l1 = [x for x,y in items]
    l2 = [y for x,y in items]
    tot = 0
    print(sum([x*l2.count(x) for x in l1]))
