def triangleCountOld(n):
	tc = n * n
	i = 2
	while i <= n:
		tc += ((n-(i-1)) * (n-(i-2))) / 2

		if n > (2 * i - 1):
			tc += ((n - (2 * i - 1)) * (n - (2 * i - 2))) / 2
		i +=1
	return tc

def diffCount(n):
	n = n-2
	if n%2 == 0:
		return (3*(n/2 - 1) + 6)
	else:
		return (3*(n/2) + 4)

tc = [0]*1000001
tc[1] = 1
tc[2] = 5
def triangleCountOld2(n):
	global tc
	if tc[n] != 0:
		return tc[n]

	val = (2*triangleCount(n-1) - triangleCount(n-2) + diffCount(n))
	tc[n] = val
	return tc[n]

def triangleCount(n):
	return (n * (n+2) * (2*n+1)) / 8

t = input()

while t > 0:
	print triangleCount(input())
	t -= 1