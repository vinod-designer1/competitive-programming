#seq 5 * (2**(n-1) - 1))
ar = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']

n = input()

if n <= 5:
	print ar[n-1]
else:
	i = 2
	m = 5 * (2**(i-1))
	while (n-m+5) > (m) :
		i += 1
		m = 5 * (2**(i-1))
	n -= (m-5)
	j = 0
	p = 2**(i-1)
	while j < 5:
		if n > ((j+1) * p) :
			j += 1
		else:
			print ar[j]
			break
