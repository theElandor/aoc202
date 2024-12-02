# took me way to long, I am to tired at 6 am :(
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
    safes = 0
    to_check = []
    for bline in grid:
        tests = []
        for i in range(len(bline)-1):
            tests.append(bline[:i] + bline[i+1:])
        tests.append(bline)
        tests.append(bline[0:-1])
        # print(tests)
        # break
        for line in tests:
            if check_line(line):
                safes += 1
                break
    print(safes)
