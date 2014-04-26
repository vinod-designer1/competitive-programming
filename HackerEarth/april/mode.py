def find_mode(ar, n):
	ar.sort()
	md = []
	mxcnt = 0
	ccnt = 0
	i = 1
	while i < n:
		if ar[i-1] == ar[i]:
			ccnt += 1
		else:
			if ccnt > mxcnt:
				md = []
				md.append(ar[i-1])
				mxcnt = ccnt
			elif ccnt == mxcnt:
				md.append(ar[i-1])
			ccnt = 0
		i += 1
	if ccnt > mxcnt:
		md = []
		md.append(ar[i-1])
	elif ccnt == mxcnt:
		md.append(ar[i-1])
	return md

t = input()

while t > 0:
	n = input()
	ar = [int(i) for i in raw_input().strip().split(' ')]
	md = find_mode(ar, n)
	md.sort(reverse=True)
	print ' '.join(str(x) for x in md)
	t -= 1



