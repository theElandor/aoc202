#horizontal, vertical, diagonal, written backwards, or even overlapping 
import re
from copy import deepcopy

def ok(i,j,grid):
    if i >= len(grid) or i < 0 or j < 0 or j >= len(grid[0]):
        return False
    return True


def get_diag(grid, si, sj, delta):
    i,j = si, sj
    diag = []
    while ok(i,j,grid):
        diag.append(grid[i][j])
        i += delta
        j += delta
    return diag
def get_main_diags(grid):
    m = []
    for i in range(len(grid)):
        j = 0
        m.append(get_diag(grid, i, j, 1))
    for j in range(1,len(grid[0])-1):
        i = 0
        m.append(get_diag(grid, i, j, 1))
    return m
with open("input.txt") as f:
    grid = [list(x) for x in f.read().splitlines()]
    rows = grid
    cols = [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]    
    m1 = get_main_diags(grid)
    revgrid = [x[::-1] for x in grid]
    m2 = get_main_diags(revgrid)
    diags = m1 + m2
    total = 0
    testing = [["." for j in range(len(grid[0]))] for i in range(len(grid))]
    for l in [rows, cols, diags]:
        for line in l:
            s = "".join(line)
            forward = [(x.start(), x.end()) for x in re.finditer("XMAS", s)]
            backwards = [(x.start(), x.end()) for x in re.finditer("SAMX", s)]
            total += len(forward)
            total += len(backwards)
    print(total)
