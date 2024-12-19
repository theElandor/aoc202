import sys
filename = sys.argv[1]
def solve(pattern, t):
	if pattern == "":
		return True
	ans = False
	for c in t:
		if pattern.startswith(c):
			ans = ans or solve(pattern[len(c):], t)
	return ans
	
with open(filename) as f:
	data = f.read().split("\n\n")
	t = data[0].split(", ")
	patterns = data[1].splitlines()
	total = 0
	print(sum([solve(p,t) for p in patterns]))
	
