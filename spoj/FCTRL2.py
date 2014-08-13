def factorial(n):
	fact = 1
	while n > 0:
		fact *= n
		n -= 1
	return fact

t = input()
while t > 0:
	print factorial(input())
	t -= 1
