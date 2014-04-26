n = input()

ar = [int(i) for i in raw_input().strip().split(' ')]

max_index = ar.index(max(ar))

i = 0

sumn = 0

while i < n:
	if max_index <= n/2:
		if i <= max_index:
			sumn += (i+(n-(max_index)))*ar[i]
		else:
			sumn += (i-max_index)*ar[i]
	else:
		if i > max_index:
			sumn += (i+(-(max_index)))*ar[i]
		else:
			sumn += (i+n-max_index)*ar[i]

	i += 1
print sumn