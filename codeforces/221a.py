def seqEle(n):
	s = str(n)
	for i in range(1, n):
		s += ' ' + str(i)
	print s

seqEle(input())