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

prmLst, primes = primes2(1000000)

a = [-1] * 1000000
a[0] = 0
a[1] = 0

def factSum(n):
    global prmLst
    global primes

    if primes[n]:
        return 1

    sumP = 1
    limit = int(n**0.5) + 1
    i = 0
    N = n
    while prmLst[i] < limit:
        powD = 0
        while n%prmLst[i] == 0:
            n /= prmLst[i]
            powD += 1
        if powD > 0:
            sumP *= ((prmLst[i]**(powD+1) - 1)/(prmLst[i]-1))
        i += 1
    return (sumP - N)


def seqVal(n):
    global a
    if a[n] != -1:
        return a[n]

    a[n] = (seqVal(n-1) + factSum(n))

    return a[n]

t = input()
for i in range(t):
    num = input()
    print seqVal(num)