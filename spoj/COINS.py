import sys

prices = [0] * 25000

def maxVal(n):
	global prices
	if n < 4:
		return n

	if n < 25000 and prices[n] != 0:
		return prices[n]

	val = maxVal(int(n/2)) + maxVal(int(n/3)) + maxVal(int(n/4))

	if val > n:
		if n < 25000:
			prices[n] = val
		return val
	else:
		if n < 25000:
			prices[n] = n
		return n

	return prices[n]

while 1:
    next = sys.stdin.readline().strip()
    if not next:
    	break
    print maxVal(int(next))