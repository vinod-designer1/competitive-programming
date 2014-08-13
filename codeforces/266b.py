nt = map(int, raw_input().strip().split())
n = nt[0]
t = nt[1]
qu = list(raw_input())
for i in range(t):
	j = 0
	while j < (n-1):
		if qu[j] == 'B':
			if qu[j+1] == 'G':
				qu[j] = 'G'
				qu[j+1] = 'B'
				j += 1
		j += 1
print ''.join(qu)