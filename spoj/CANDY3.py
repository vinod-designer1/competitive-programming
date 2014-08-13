tc = input()
while tc > 0:
	bl = raw_input()
	t = input()
	ars = 0

	i = t
	while i > 0:
		n = input()
		ars += n

		i -= 1
	avg = (ars)/(t)
	if (t * avg) == ars:
		print 'YES'
	else:
		print 'NO'
	tc -= 1