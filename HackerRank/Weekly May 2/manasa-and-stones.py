#https://www.hackerrank.com/contests/w2/challenges/manasa-and-stones
def possibleValues(n, a, b):
	poss_values = []

	if a == b:
		poss_values.append((n-1) * a)
	else:
		p = n-1
		k = 0
		if a > b:
			temp = a
			a = b
			b = temp
		while p >= 0:
			val = p*a+k*b
			if val not in poss_values:
				poss_values.append(val)
			p -= 1
			k += 1
	return poss_values

t = input()

while t > 0:
	n = input()
	a = input()
	b = input()
	print " ".join(str(x) for x in possibleValues(n, a, b))

	t -= 1


