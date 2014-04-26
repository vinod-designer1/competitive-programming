#http://www.spoj.com/problems/LASTDIG2/
def ltdig(a, b):
	if b == 0 and a!=0:
		return 1
	else:
		if a == 0:
			return 0
		r = a%10
		if r == 1:
			return 1
		elif r == 5:
			return 5
		elif r == 6:
			return 6
		else:
			r = b%4
			if r == 0:
				if a%2==0:
					return 6
				else:
					return 1
			elif r == 1:
				return (a)%10
			elif r == 2:
				return (a * a)%10
			elif r == 3:
				return (a * a * a)%10
t = input()

i = 0
while i < t:
	ab = [int(n) for n in raw_input().strip().split(' ')]
	print ltdig(ab[0], ab[1])
	i += 1
