t = input()

while t > 0:
	n = input()
	ar = [int(i) for i in raw_input().strip().split(' ')]
	ar.sort(reverse=True)
	max_ar = ar[0]
	sum_ar = sum(ar)
	i = 0
	sum_ab_d = 0
	prev_sum = ar[0]
	while i < n-1:
		sum_ab_d += abs((ar[i]*(n-(i+1))) - (sum_ar - prev_sum))
		prev_sum += ar[i+1]
		i += 1
	print (sum_ab_d * max_ar)%(1000000007)
	t -= 1