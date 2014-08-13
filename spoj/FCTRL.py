def find_no_trailing_zeros_factorial(N):
	''' find power of 5 in n! '''
	five_cnt = 0
	i = 5
	while i <= N:
		five_cnt += (N/i)
		i *= 5
	return five_cnt 

t = input()

while t > 0:
	n = input()
	print find_no_trailing_zeros_factorial(n)
	t -= 1