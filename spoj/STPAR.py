def canOrder(cord, nTrk):
	ordT = []
	sL = []

	for i in cord:
		if not ordT:
			if i == 1:
				ordT.append(i)
			else:
				if sL:
					p = sL.pop()
					if p < i:
						return 'no'
					sL.append(p)
				sL.append(i)
		else:
			s = ordT.pop()
			if  i == s+1:
				ordT.append(s)
				ordT.append(i)
			else:
				ordT.append(s)
				if not sL:
					sL.append(i)
				else:
					p = sL.pop()
					while p > 0 and p < i:
						s = ordT.pop()
						if  p == s + 1:
							ordT.append(s)
							ordT.append(p)
						else:
							return 'no'
						if sL:
							p = sL.pop()
						else:
							p = -1
					if  p == -1:
						sL.append(i)
					else:
						sL.append(p)
						sL.append(i)
	return 'yes'

t = input()

while t != 0:
	cord = map(int, raw_input().split())
	print canOrder(cord, t)

	t = input()