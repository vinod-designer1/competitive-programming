def nearestPalin(n):
	nL = len(n)

	if nL == 1:
		n = int(n)
		if n == 9:
			return '11'
		else:
			return (n + 1)

	mid = nL / 2
	nEven = False

	eMid = mid

	limit = mid + 1

	if nL % 2 == 0:
		eMid -= 1
		limit = mid
		nEven = True
	
	i = 0
	m = ''
	nz = ''
	nc = 0
	ns = False

	while i < limit:
		l = (eMid-i)
		r = (mid+i)

		lN = int(n[l])
		rN = int(n[r])

		if lN > rN:
			n = n[:(eMid+1)]
			ns = False
			break
		elif lN < rN:
			#n = n[:l] + str(lN+1) + m
			ns = False
			i = limit
			break
		else:
			m += '0'
			if l == (eMid):
				if lN == 9:
					ns = True
					nz += '0'
					nc += 1

			else:
				if ns:
					if lN == 9:
						nz += '0'
						nc += 1
					else:
						ns = False
		i += 1

	if nEven:
		if i == limit:
			if nc > 0:
				if ns:
					n = '1' + nz + nz[:(nc-1)] + '1'
				else:
					n = n[:(eMid+1)]
					n = n[:-(nc+1)] + str(int(n[-(nc+1)])+1) + nz
					n += n[::-1]
			else:
				n = n[:eMid] + str(int(n[eMid])+1)
				n += n[::-1]
		else:
			n += n[::-1]
	else:
		if i == limit:
			if nc > 0:
				if ns:
					n = '1' + nz +  nz[:(nc-2)] + '1'
				else:
					n = n[:(eMid+1)]
					n = n[:-(nc+1)] + str(int(n[-(nc+1)])+1) + nz[:(nc-1)]
					n += '0' + n[::-1]
			else:
				m = str(int(n[eMid])+1)
				n = n[:eMid]
				n += m + n[::-1]
		else:
			m = n[-1]
			n = n[:eMid]
			n += m + n[::-1]

	return n


t = input()

while t > 0:
	print nearestPalin(raw_input())
	t -= 1