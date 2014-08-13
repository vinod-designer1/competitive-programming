def noOfFactors(n):
	limit = int(n ** 0.5) + 1
	i = 1
	cnt = 0
	while i < limit:
		if n % i == 0:
			cnt += 2
		i += 1
	return cnt

def noSquares(n):
	i = 2
	noSq = 1 
	while i <= n:
		noF = noOfFactors(i)
		noSq += noF/2
		i += 1
	return noSq

print noSquares(input())
