def check_line(line):
    if any([x==y for x,y in zip(line[:-1], line[1:])]):
        return False
    if (line != sorted(line) and line != sorted(line, reverse=True)):
        return False
    diffs = [abs(x-y) for x,y in zip(line[:-1], line[1:])]
    if any([x > 3 for x in diffs]): return False
    return True

with open ("input.txt") as f:
    grid = [[int(x) for x in list(y.split())] for y in f.read().splitlines()]
    safes = sum([check_line(line) for line in grid])
    print(safes)
