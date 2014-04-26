#https://www.hackerrank.com/challenges/icecream-parlor

def findIndexes(ary, n, m):
	cary = ary[:]
	ary.sort()
	st = 0
	end = n-1
	while st != end and st < end:
		sm = ary[st] + ary[end]
		if sm < m:
			st += 1
		elif sm > m:
			end -= 1
		else:
			break
	fin = cary.index(ary[st])
	cary[fin] = -1
	lin = cary.index(ary[end])

	print fin+1,lin+1

t = input()

for i in range(t):
	m = input()
	n = input()
	ar = [int(i) for i  in raw_input().strip().split(' ')]
	findIndexes(ar, n, m)

