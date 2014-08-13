def assign_rank(ar, rnk, ind):
	if rnk[ind] == -1:
		if ar[ind] == 0:
			rnk[ind] = 1
		else:
			rnk[ind] = 1 + assign_rank(ar, rnk, ar[ind]-1)
	return rnk[ind]

t = input()

while t > 0:
	n = input()
	rnk = [-1]*n
	ar = [int(i) for i in raw_input().strip().split(' ')]
	i = 0
	while i < n:
		assign_rank(ar, rnk, i)
		i += 1
	q = input()
	while q > 0:
		nm = [int(j) for j in raw_input().strip().split(' ')]
		n = nm[0] - 1
		m = nm[1] - 1
		if rnk[n] <= rnk[m]:
			print -1
		else:
			print (rnk[n] - rnk[m] - 1)
		q -= 1
	t -= 1
