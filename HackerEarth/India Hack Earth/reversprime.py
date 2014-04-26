#emrip numbers revers primes
def reverse(prime, is_prime):
	if prime > 10 and is_prime[prime]:
		rev = 0
		num = prime
		while(num > 0):
			rev = (10*rev)+num%10
			num //= 10
		if is_prime[rev]:
			if rev < prime:
				return False
			return True
	return False

def primes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1) 
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if reverse(i, is_prime)]


ary = primes_upto(10**7)

for i in ary:
	print i