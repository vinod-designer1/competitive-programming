def kThNumber(k):
	return (250 * (k-1) + 192)

t = input()
while t > 0:
	print kThNumber(input())
	t -= 1