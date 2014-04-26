#https://www.hackerrank.com/challenges/is-fibo
import math

fib = [1, 1]

def genFib(fst, lst):
	global fib
	if len(fib) < 50:
		fib.append(fst+lst)
		genFib(lst, (fst+lst))
	else:
		return 0

def isPerfectSq(x):
	s = math.sqrt(x)
	print s
	print s*s
	return s * s == (x*1.0)

def isFibanocciNum(n):
	return n in fib

genFib(1, 1)

print fib

t = input()

while t > 0:
	if isFibanocciNum(input()):
		print 'IsFibo'
	else:
		print 'IsNotFibo'
	t -= 1