#https://www.hackerrank.com/challenges/picking-cards

t = input()

for i in range(t):
	n = input()
	ar = [int(i) for i in raw_input().strip().split(' ')]
	nar = [0]*(n+1)
	for i in ar:
		nar[i] += 1
	prdct = 1
	cnt = 0
	fail = False
	for i in range(n):
		if cnt < i:
			fail = True
			break
		else:
			cnt += nar[i]
			prdct *= (cnt-i)
			
	if nar[n] != 0:
		cnt += nar[n]
		prdct *= (cnt-n)

	if not fail:
		print prdct%(10**9+7)
	else:
		print 0
