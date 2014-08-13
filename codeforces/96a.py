st = raw_input()
stL = len(st)
prev = st[0]
cnt = 1
y = False
for i in range(1, stL):
	if st[i] == prev:
		cnt += 1
	else:
		cnt = 1
	if cnt == 7:
		y = True
		break
	prev = st[i]

if y:
	print 'YES'
else:
	print 'NO'