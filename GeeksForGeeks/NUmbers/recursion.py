def print_100_without_loop(st):
	if st > 100:
		return 0
	else:
		print st
		print_100_without_loop(st + 1)

def sumof_digits_number_single_statement(num):
	#for sumn=0 and n > 0 and (sumn+=n%10 and n/=10):
	#	pass
	return 0 if num == 0 else num%10 + sumof_digits_number_single_statement(num/10)

def power(x, n):
	if n==0:
		return 1

	s = power(x, n/2)
	res = s*s

	if n%2 != 0:
		res *= x
	return res

print power(10, 1000)
