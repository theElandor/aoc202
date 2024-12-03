import re
with open("input.txt") as f:
    data = f.read()
    print(data)
    matches = re.findall("mul\(\d+,\d+\)", data)
    s = 0
    for m in matches:
        x,y = m[4:-1].split(",")
        s += int(x)*int(y)
    print(s)
