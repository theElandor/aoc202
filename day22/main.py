import sys
from collections import deque
filename = sys.argv[1]
def prune(x):
	return x % 16777216
def mix(n,x):
	return x ^ n
def secret(n,t):
	res = []
	prev = int(str(n)[-1])
	for next in range(t):
		n = prune(mix(n, n*64))
		n = prune(mix(n, n//32))
		n = prune(mix(n, n*2048))
		res.append((int(str(n)[-1]),int(str(n)[-1]) - prev))
		prev = int(str(n)[-1])
	return res

def update(m, Q, s, right,f):
	if f not in m:
		m[f] = [s[right][0]]
	else:
		m[f].append(s[right][0])

with open(filename) as f:
	numbers = [int(x) for x in f.read().splitlines()]
	m = {}
	for n in numbers:
		seen = set()
		s = secret(n, 2000)
		left = 0
		Q = deque()
		for i in range(4):
			Q.append(s[i][1])
		f = tuple(Q)
		update(m, Q, s,3,f)
		seen.add(f)
		for right in range(4, len(s)):
			Q.popleft()
			Q.append(s[right][1])
			f = tuple(Q)
			if f in seen: continue
			update(m, Q, s,right,f)
			seen.add(f)
	l = []
	for k, v in m.items():
		l.append((sum(v), k))
	print(sorted(l,reverse=True)[0])

			
		
		
		
