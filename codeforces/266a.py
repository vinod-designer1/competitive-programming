def stnRem(st, stL):
	rem = 0
	prev = st[0]
	for i in range(1, stL):
		if prev == st[i]:
			rem += 1
		else:
			prev = st[i]
	return rem

stL = input()
print stnRem(raw_input(), stL)