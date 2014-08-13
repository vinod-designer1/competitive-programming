def isAmbigous(ar, ln):
	na = False
	for i in xrange(ln):
		if ar[ar[i] - 1] != (i+1):
			na = True
	if na:
		return 'not ambiguous'
	else:
		return 'ambiguous'

t = input()

while t!= 0:
	ar = [int(i) for i in raw_input().strip().split(' ')]
	print isAmbigous(ar, t)

	t = input()