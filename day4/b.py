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
    return diag, si, sj

def get_main_diags(grid):
    f = [get_diag(grid, i, 0,1) for i in range(len(grid))]
    s = [get_diag(grid, 0, j,1) for j in range(1,len(grid[0])-1)]
    return f+s

with open("input.txt") as f:
    grid = [list(x) for x in f.read().splitlines()]
    rows = grid
    cols = [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]    
    m1 = get_main_diags(grid)
    revgrid = [x[::-1] for x in grid]
    m2 = get_main_diags(revgrid)    
    total = 0
    testing = [["." for j in range(len(grid[0]))] for i in range(len(grid))]
    m1_coords = set()
    for line, i, j in m1:
        s = "".join(line)
        f = [(x.start()) for x in re.finditer("MAS", s)]
        b = [(x.start()) for x in re.finditer("SAM", s)]
        for s in f+b:            
            m1_coords.add((i+s, j+s))
    for line, i, j in m2:
        s = "".join(line)   
        f = [(x.start()) for x in re.finditer("MAS", s)]
        b = [(x.start()) for x in re.finditer("SAM", s)]
        for s in f+b:
            rx,ry = (i+s, j+s)
            if (rx, len(grid[0])-ry-3) in m1_coords:
                total += 1            
    print(total)