n = raw_input()
nL = len(n)

cnt = 0
while len(n) != 1:
	s = 0
	for i in n:
		s += int(i)
	n = str(s)
	cnt += 1
print cnt
