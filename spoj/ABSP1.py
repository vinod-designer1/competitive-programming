def ABS(ar, n):
	abd = ar[1] - ar[0]
	i = 2
	prev = abd
	for i in range(2,n):
		prev = prev + i * (ar[i] - ar[i-1])
		abd += prev
	return abd

t = input()
for i in range(t):
	n = input()
	ar = map(int, raw_input().split())
	print ABS(ar, n)