import re
def get_value(s):
    x,y = s[4:-1].split(",")
    return int(x)*int(y)

with open("input.txt") as f:
    data = f.read()
    matches = [(x.start(), x.group()) for x in re.finditer("mul\(\d+,\d+\)", data)]
    dos = [(x.start(), "do") for x in re.finditer("do\(\)", data)    ]
    donts  = [(x.start(), "dont") for x in re.finditer("don\'t\(\)", data)]
    stuff = (matches + dos + donts)
    slist = sorted(stuff, key=lambda x:x[0])
    s = 0 
    enabled = True
    for start, command in slist:
        if command.startswith("mul") and enabled:
            print(command)
            s += get_value(command)
        else:
            enabled = True if command = "do" else False
    print(s)
