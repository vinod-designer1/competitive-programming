#https://www.hackerrank.com/challenges/sherlock-and-the-beast
def large_decent_number(k):
	f = k/3
	while f > -1 and (k-3*f)%5 !=0:
		f -= 1
	if f < 0:
		f = 0
	if (k - 3*f)%5 !=0:
		return -1
	else:
		return '5'*(3*f) + '3'*(k - 3*f)

t = input()

while t > 0:
	print large_decent_number(input())
	t -= 1