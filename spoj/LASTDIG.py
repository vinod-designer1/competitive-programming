def lastDigitOld(a, b):
	a = a%10
	if a == 0 or a == 1 or a == 5 or a == 6:
		return a
	elif a == 2 or a == 3 or a == 7 or a == 8:
		r = b%4
		if a == 2:
			return (6 if r == 0 else 2 if r == 1 else 4 if r == 2 else 8)
		if a == 3:
			return (1 if r == 0 else 3 if r == 1 else 9 if r == 2 else 7)
		if a == 7:
			return (1 if r == 0 else 7 if r == 1 else 9 if r == 2 else 3)
		if a == 8:
			return (6 if r == 0 else 8 if r == 1 else 4 if r == 2 else 2)
	elif a == 4 or a == 9:
		r = b%2
		if a == 4:
			return (6 if r == 0 else 4)	
		if a == 9:
			return (1 if r == 0 else 9)

def modexp(a, n, m):
	bits = []
	while n:
		bits.append(n%2)
		n /= 2
	solution = 1
	bits.reverse()
	for x in bits:
		solution = (solution*solution)%m
		if x:
			solution = (solution*a)%m
	return solution

t = input()
while t > 0:
	ab = [int(i) for i in raw_input().strip().split(' ')]
	print modexp(ab[0], ab[1], 10)
	t -= 1