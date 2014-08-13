def hagover(c):
	s = 2.0
	d = 1/s
	while c > d:
		s += 1
		d += (1/s)
	return int(s-1)

t = input()

while t != 0.00:
	print hagover(t), 'card(s)'
	t = input()
