n = input()
ar = [int(i) for i in raw_input().strip().split()]

p = [0]*4

for i in ar:
    p[i-1] += 1

countn = p[3]

countn += p[2]

p[0] = - p[2] + p[0]

 
if p[1]%2 == 0:
    countn += (p[1]/2)
else:
    countn += ((p[1]-1)/2)
    countn += 1
    p[0] -= 2

if p[0] > 0:
    countn += (p[0]/4)
    if p[0]%4 != 0:
        countn += 1

print countn
        
