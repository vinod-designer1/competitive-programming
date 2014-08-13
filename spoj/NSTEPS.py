def pointValue(x, y):
	if x > 10000 or y > 10000 or x < 0 or y < 0 or x < y or ((x-y) != 2 and  (x-y) != 0):
		return 'No Number'

	if x%2 == 0:
		return y+x
	else:
		return (y+x-1)

t = input()

while t > 0:
	ab = [int(i) for i in raw_input().strip().split(' ')]
	print pointValue(ab[0], ab[1])

	t -= 1