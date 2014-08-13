def unLucky(num, nL):
	mid = nL/2
	c = [cmp(a, b) for a, b in zip(sorted(num[0 : mid]), sorted(num[mid : ]))]
	return 'YES' if min(c) == max(c) and min(c) else 'NO'
nL = input()
num = raw_input()
print unLucky(num, 2*nL)