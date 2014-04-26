#https://www.hackerrank.com/challenges/bday-gift
# to no of time we add each number will be 2^n-1
# so total possibilit are 2^n so total is sum/2

n = input()

sumn = 0

for i in range(n):
	sumn += input()

print sumn/2.0