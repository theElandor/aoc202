# took me way to long, I am to tired at 6 am :(
def check_line(line):
    if line[0] > line[1]: order = "dec"
    elif line[0] < line[1]: order = "inc"
    else: return False
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            return False
        elif line[i] > line[i+1] and order == "inc":
            return False
        elif line[i] < line[i+1] and order == "dec":
            return False
    for i in range(0, len(line)-1):
        if abs(line[i]-line[i+1]) > 3:
            return False
    else:
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
                print(line)
                safes += 1
                break
    print(safes)
