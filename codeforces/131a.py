def changeCase(st):
	stL = len(st)
	nU = 0
	for c in st:
		if c >= 'A' and c <= 'Z':
			nU += 1

	if nU == stL:
		return st.lower()

	if (nU == (stL-1) and (st[0] >= 'a' and st[0] <= 'z')):
		return st[0].upper() + st[1:].lower()

	return st

print changeCase(raw_input())