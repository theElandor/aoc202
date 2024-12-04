# better solution!
def ok(i,j,grid):
    if i >= len(grid) or i < 0 or j < 0 or j >= len(grid[0]):
        return False
    return True

with open("input.txt") as f:
    total = 0
    grid = [list(x) for x in f.read().splitlines()]
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] != "A": continue
            w1 = ""
            for di, dj in (-1,-1),(1,1):
                if ok(i+di, j+dj, grid):
                    w1+=grid[i+di][j+dj]
            w2 = ""
            for di, dj in (-1,1),(1,-1):
                if ok(i+di, j+dj, grid):
                    w2+=grid[i+di][j+dj]
            if (w1 == "SM" or w1 == "MS") and (w2 == "SM" or w2 == "MS"):
                total += 1
    print(total)