#http://www.spoj.com/problems/PRIME1/
import math
import Queue
import time

def primeGenerator(n):
	result = [0] * (n+1)
	primes = [2,3]
	seq = [2, 4]
	limit = int(math.sqrt(n))

	for x in range(1, limit/4 + 1):
		k1 = 4 * x * x
		for y in range(1, limit - k1 + 1, 2):
			s = 4 * x * x + y * y
			if s <= n and ( s%12 == 1 or s%12 == 5):
				result[s] ^= 1

	for x in range(1, limit/3 + 1):
		k1  = 3 * x * x
		y = 2
		i = 0
		while y <= (limit-k1):
			s = k1 + y * y
			if s <= n and ( s%12 == 7):
				result[s] ^= 1
			y += seq[i%2]
			i += 1

	for x in range(1, limit + 1):
		y = 1
		c = 1
		i = 0
		if x%2 != 0:
			y = 2
			c = 0
		while y < x + 1:
			s = 3 * x * x - y * y
			if (x > y) and (s <= n) and (s%12 == 11):
				result[s] ^= 1
			y += seq[(i+c)%2]
			i += 1
    
	for i in range(5, limit):
		if result[i]:
			j = 1
			k = j * i * i
			while k <= n:
				result[k] = 0
				j += 1
				k = j * i * i

	return result

def sieveOfEratosthenes(limit):
	primes = [True]*(limit+1)
	primes[0] = False
	primes[1] = False
	for i in range(2, int(limit ** 0.5) + 1):
		if primes[i]:
			for j in range(i*i, limit+1, i):
				primes[j] = False
	return primes

##odd only vesion of sieve of Eratosthenes
def primes2(limit):
    if limit < 2: return []
    if limit < 3: return [2]
    lmtbf = (limit - 3) // 2
    buf = [True] * (lmtbf + 1)
    primes = [False] * (limit + 1)
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)
    prmLst = [2] + [i + i + 3 for i, v in enumerate(buf) if v]

    for i in prmLst:
    	primes[i] = True
    return prmLst, primes

def segmentedSieve(m, n, primes):
	diff = n - m + 1 
	segPrimes = [True] * (diff)
	maxPrime = int(n ** 0.5)
	i = 0
	while primes[i] <= maxPrime:
		p = primes[i]
		sti = m - (m // p) * p
		if sti != 0:
			sti = p - sti

		while sti < diff:
			segPrimes[sti] = False
			sti += p
		i += 1

	prmLst = []
	i = 0
	while i < diff:
		if segPrimes[i]:
			prmLst.append(m+i)
		i += 1

	return prmLst

prmLst, primes = primes2(100000)

t = input()

while t > 0:
	ab = [int(i) for i in raw_input().strip().split(' ')]
	i = ab[0]

	while i < (ab[1] + 1):
		if i <= 100000:
			if primes[i]:
				print i
		else:
			segPrimes = segmentedSieve(i, ab[1], prmLst)
			for j in segPrimes:
				print j
			break
		i += 1
	t -= 1
	print ''
	print ''