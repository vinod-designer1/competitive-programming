def modexp(a, n, m):
	bits = []
	while n:
		bits.append(n%2)
		n /= 2
	solution = 1
	bits.reverse()
	for x in bits:
		solution = (solution*solution)%m
		if x:
			solution = (solution*a)%m
	return solution

def isprime(n):
   """Returns True if n is prime"""
   if n == 2: return True
   if n == 3: return True
   if n % 2 == 0: return False
   if n % 3 == 0: return False

   i = 5
   w = 2
   while i * i <= n:
      if n % i == 0:
         return False

      i += w
      w = 6 - w

   return True

N = 600851475143
srN = int(N**0.5)
maxP = 0
for i in range(2, srN+1):
    if N%i == 0:
    	if isprime(i):
    		if maxP < i:
    			maxP = i
        if isprime(N/i):
            if maxP < (N/i):
    			maxP = (N/i)
print maxP