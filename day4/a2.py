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
            if grid[i][j] != "X": continue
            for di, dj in [(-1,0),(1,0),(0,-1), (0,1),(-1,1),(1,1),(1,-1),(-1,-1)]:
                word = ""
                for dist in range(1,4):
                    if ok(i+di*dist, j+dj*dist, grid):
                        word += grid[i+di*dist][j+dj*dist]
                if word == "MAS":
                    total += 1
    print(total)