def armiesWonOld(army1, army1len, army2, army2len):
	army1.sort()
	army2.sort()

	i = 0
	j = 0

	while i < army1len and j < army2len:
		if army2[j] > army1[i]:
			i += 1
		else:
			j += 1

	if i == army1len:
		return 'MechaGodzilla'
	else:
		return 'Godzilla'

def armiesWon(army1, army1len, army2, army2len):
	army1Max = max(army1)
	army2Max = max(army2)

	if army2Max > army1Max:
		return 'MechaGodzilla'
	else:
		return 'Godzilla'

t = input()
while t > 0:
	bl = raw_input()

	ab = map(int, raw_input().split())
	arm1 = map(int, raw_input().split())
	arm2 = map(int, raw_input().split())
	print armiesWon(arm1, ab[0], arm2, ab[1])

	t -= 1