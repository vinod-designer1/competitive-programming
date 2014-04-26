'''
Algorithm: getParity(n)
1. Initialize parity = 0
2. Loop while n != 0      
      a. Invert parity 
             parity = !parity
      b. Unset rightmost set bit
             n = n & (n-1)
3. return parity

Example:
 Initialize: n = 13 (1101)   parity = 0

n = 13 & 12  = 12 (1100)   parity = 1
n = 12 & 11 = 8  (1000)   parity = 0
n = 8 & 7 = 0  (0000)    parity = 1
'''