def reverse_num(a):
	rev_num = 0
	while a!=0:
		rev_num = rev_num*10+(a%10)
		a /= 10
	return rev_num

t = input()

while t > 0:
	ar = [int(i) for i in raw_input().strip().split(' ')]
	sum_rev = reverse_num(ar[0]) + reverse_num(ar[1])
	print reverse_num(sum_rev)
	t -= 1