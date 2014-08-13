facts = []
for i in range(2001):
	facts.append([]*2001)

def factorsLs(n):
	global facts
	if facts[n]:
		return facts[n]
	i = 1
	fact = []
	while i * i <= n:
		if n%i == 0:
			fact.append(i)
			if i != 1 and i != (n/i):
				fact.append(n/i)
		i += 1
	facts[n] = fact
	return fact

ways = []
for i in range(2001):
	ways.append([0]*2001)

def noWays(n,k):
	global ways
	if n == 1:
		return 1

	if ways[n][k] != 0:
		return ways[n][k]

	sol = 1
	facts = factorsLs(n)

	for fact in facts:
		for i in range(1, k):
			s = noWays(fact,i)
			sol += s

	ways[n][k] = sol

	return sol

def tways(n,k):
	sumv = 0
	for i in range(1,n+1):
		s = noWays(i,k)
		print 'sol', i, k, s
		sumv += s
	return sumv

n,k = map(int, raw_input().split())
print tways(n,k)
n,k = map(int, raw_input().split())
print tways(n,k)
	
