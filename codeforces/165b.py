n,k = map(int, raw_input().split())

l = 1
r = n
while l < r:
	v = (r+l)//2
	s = 0
	p = v
	while p:
		s += p
		p //= k
	if s < n:
		l = v + 1
	elif s >= n:
		r = v
print r
