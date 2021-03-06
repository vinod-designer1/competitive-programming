n = input()
lo, hi = -2*10**9, 2*10**9
inv = {">=":"<", ">":"<=", "<":">=", "<=":">"}
for i in range(0, n):
	op, x, truth = raw_input().split()
	x = int(x)
	if truth == "N": op = inv[op]

	if '<' in op:
		if op == '<': x -= 1
		hi = min(hi, x)
	if '>' in op:
		if op == '>': x += 1
		lo = max(lo, x)

print lo if lo <= hi else "Impossible"