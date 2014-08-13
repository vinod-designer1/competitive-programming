def finalPos(st, ins):
	i = 0
	for c in ins:
		if c == st[i]:
			i += 1
	return (i+1)

print finalPos(raw_input(), raw_input())