def gcd(a,b):
	sm = a
	bg = b
	if a > b:
		sm = b
		bg = a

	r = bg%sm
	while r != 0:
		bg = sm
		sm = r
		r = bg%sm
	return sm

a, b, n = map(int, raw_input().strip().split())

t = 1
r = gcd(a,n)

while n >= r:
	n -= r
	if n == 0:
		t += 1
		break
	if t%2 == 1:
		r = gcd(b,n)
	else:
		r = gcd(a,n)
	t += 1
if t%2 == 0:
	print 0
else:
	print 1