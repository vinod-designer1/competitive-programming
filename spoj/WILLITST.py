def isPos(n):
	if n <= 1:
		return 'TAK'

	if (n & (n-1)) == 0:
		return 'TAK'
	else:
		return 'NIE'


print isPos(input())
