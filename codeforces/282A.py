t = input()
res = 0
for i in range(t):
	op = raw_input().strip()

	if op[1] == '-':
		res -= 1
	else:
		res += 1

print res