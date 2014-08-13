def getSeq(trt, ltrt, sumS):
	sumTrm = trt + ltrt
	nt = (2 * sumS) / sumTrm
	diff  = ltrt - trt
	d = (diff/ (nt - 5))
	a = trt - (2 * d)

	seq = ''
	for i in range(nt):
		seq += str(a + i * d) + ' '

	print nt
	print seq.strip() 

t = input()

while t > 0:
	ar = map(int, raw_input().split())
	getSeq(ar[0], ar[1], ar[2])

	t -= 1