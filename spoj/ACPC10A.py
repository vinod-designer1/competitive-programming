def whichSeq(ar):
	diff1 = ar[1] - ar[0]
	diff2 = ar[2] - ar[1]
	if diff1 == diff2:
		nxtNum = ar[0] + diff1 * 3
		return 'AP', nxtNum

	rt1 = ar[1]/ar[0]
	rt2 = ar[2]/ar[1]
	if rt1 == rt2:
		nxtNum = ar[0] * (rt1**3)
		return 'GP', nxtNum

ar = [int(i) for i in raw_input().strip().split(' ')]

while not (ar[0] == 0 and ar[1] == 0 and ar[2] == 0):
	seq, nxtNum = whichSeq(ar)

	print seq, nxtNum

	ar = [int(i) for i in raw_input().strip().split(' ')]

