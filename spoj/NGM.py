def numberGame(N):
	r = N%10
	if r == 0:
		print 2
	else:
		print 1
		print r

numberGame(input())