with open ("input.txt") as f:
    grid = [[int(x) for x in list(y.split())] for y in f.read().splitlines()]
    safes = 0
    to_check = []
    for line in grid:
        # check increasing / decreasing
        if line[0] > line[1]: order = "dec"
        elif line[0] < line[1]: order = "inc"
        else: continue
        for i in range(1, len(line)-1):
            if line[i] == line[i+1]:
                break
            elif line[i] > line[i+1] and order == "inc":
                break
            elif line[i] < line[i+1] and order == "dec":
                break
        else:
            to_check.append(line)
    for line in to_check:
        for i in range(0, len(line)-1):
            if abs(line[i]-line[i+1]) > 3:
                break
        else:
            print(line)
            safes += 1
    print(safes)
            
            
