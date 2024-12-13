import sys
import time
import math
from sympy import *
from sympy.solvers.solveset import linsolve
filename = sys.argv[1]
# At first, I realized this was some sort of math-trick puzzle.
# Then I did the diligent thing, aka implementing a DP solution for the first part.
# The problem is that I lost a lot of time trying to prune the search for the second part,
# but haven't found any way to do it. Then I tried to write the equations and realized it was
# just a system of 2 equations with 2 unknowns...the thing that misslead me was the "find the MINIMUM"
# number of things needed.
# Learned simpy though, since I did not have pen and paper in my hotel room to solve this :)
with open(filename) as f:
    data = f.read().split("\n\n")
    s = {}
    for i, d in enumerate(data):
        s[i] = {"A":[], "B":[]}
        for line in d.splitlines():
            if line.startswith("Button"):
                letter = line.split(":")[0][-1]
                commands = [x.strip() for x in line.split(":")[1].split(",")]
                s[i][letter] = commands
            else:
                prize = [x.strip() for x in line.split(":")[1].split(",")]
                s[i]["prize"] = prize
    t = 0
    for i,(test, sett) in enumerate(s.items()):
        print(f"{i}/{len(s.items())}")
        tx, ty = [int(x[2:])+10000000000000 for x in sett["prize"]]
        dax, day = [int(x[2:]) for x in sett["A"]]
        dbx, dby = [int(x[2:]) for x in sett["B"]]
        m,n = symbols('m, n')
        sol = linsolve([(m * dax)+(n*dbx)-tx,(m * day)+(n*dby)-ty],(m,n))
        for x in sol:
            a_tokens, b_tokens = x
            if a_tokens.is_integer and b_tokens.is_integer:
                t += (a_tokens*3) + (b_tokens)
            break
    print(t)
