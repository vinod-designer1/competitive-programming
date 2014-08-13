def getTerm(n):
	r = (((1+(n*4*2))**0.5)+1)/2
	if int(r) == r:
		r = r-1
	r = int(r)
	st = (r * (r-1))/2 + 1
	diff = n - st

	if r%2 == 0:
		return str(1+diff) + '/' + str(r-diff)
	else:
		return str(r-diff) + '/' + str(1+diff)

t = input()

while t > 0:
	n = input()
	print 'TERM', n, 'IS', getTerm(n)
	
	t -= 1