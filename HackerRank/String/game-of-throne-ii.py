#!/usr/bin/py
from collections import Counter

mod = 10**9 + 7

def hasPalindrome(word):
    x = Counter(word)
    count = 0
    for i in x:
        if x[i]%2!=0:
            count += 1

    if count > 1:
        return False
    else:
        return True

def getfactmod(b):
    val = 1
    for i in range(1,b):
        val =((val%mod)*((i+1)%mod))%mod

    return val

def getpowermod(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a
    temp = getpowermod(a,b/2)
    if b%2==0:
        return ((temp%mod)**2)%mod
    else:
        return (a*((temp%mod)**2))%mod

def inversemod(a):
    return getpowermod(a,mod-2)

if __name__ == '__main__':
    word = raw_input()
    assert 1 <= len(word) <= 10**5
    assert hasPalindrome(word) == True
    counter = Counter(word)
    denominator = 1
    numerator = 0
    for i in counter:
        numerator += counter[i]/2
        denominator = ((denominator%mod)*(getfactmod(counter[i]/2)%mod))%mod

    numerator = getfactmod(numerator)
    answer = ((numerator%mod)*(inversemod(denominator)%mod))%mod
    print answer