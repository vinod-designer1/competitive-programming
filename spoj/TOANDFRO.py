def decrypt(st, gap):
	stLen = len(st)
	os = ''
	i = 0
	while i < gap:
		j = i
		while j < stLen:
			if j < gap or (j + 1 + (2 * i)) >= stLen:
				os += st[j]
			else:
				os += st[j] + st[j + 1 + (2 * i)]
				j += 1 + (2 * i)

			j += (gap - (i + 1)) * 2 + 1
		i += 1
	return os

t = -1

while t != 0:
	t = input()
	if t!= 0:
		st = raw_input()
		print decrypt(st, t)