#https://www.hackerrank.com/challenges/find-digits
def findDigits(num):
	cnum = num
	cnt = 0
	while num != 0:
		r = num%10
		if r!=0  and  cnum%r == 0:
			cnt += 1
		num /= 10
	return cnt

t = input()

while t > 0:
	num = input()
	print findDigits(num)
	t -= 1
