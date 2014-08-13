def minChc(ar, avg):
	noC = 0

	for i in ar:
		if i < avg:
			noC += (avg - i)
	return noC

t = 0
while t != -1:
	t = input()
	if t != -1:
		ar = []
		ars = 0

		i = t
		while i > 0:
			n = input()
			ar.append(n)
			ars += n

			i -= 1
		avg = ars/t

		if (t * avg) == ars:
			r = minChc(ar, int(avg))
			print r
		else:
			print -1
