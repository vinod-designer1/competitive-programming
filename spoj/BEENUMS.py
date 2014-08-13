#1+6+12+18+..
def isBeehiveNum(N):
	if (N-1)%6 != 0:
		return 'N'
	else:
		k = (N-1) / 6
		p = 1 + 8 * k

		s = int(p ** 0.5)

		if s*s == p:
			return 'Y'
		else:
			return 'N'

N = input()
while N != -1:
	print isBeehiveNum(N)

	N = input()