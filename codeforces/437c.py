n,m = map(int, raw_input().split())
v = [0]+map(int, raw_input().split())
ar = [0]*n
s = 0

for i in range(m):
	x,y = map(int, raw_input().split())
	s += min(v[x], v[y])
print s