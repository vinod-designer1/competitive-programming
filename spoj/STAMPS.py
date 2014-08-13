def stampsBorrow(stc, pl, need):
	stc.sort()
	i = pl-1
	ct = 0
	while i >= 0:
		ct += stc[i]
		if ct >= need:
			return (pl-i)
		i -= 1
	return 'impossible'

t = input()

i = 1
while i <= t:
	ab = [int(j) for j in raw_input().strip().split(' ')]
	stc = [int(j) for j in raw_input().strip().split(' ')]
	print 'Scenario', '#' + str(i) + ':'
	print stampsBorrow(stc, ab[1], ab[0])

	i += 1