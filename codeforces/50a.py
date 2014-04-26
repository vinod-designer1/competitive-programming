mn = [int(i) for i in raw_input().strip().split()]
m = mn[0]
n = mn[1]

if m%2 == 0:
    s = m/2
    print s*n
elif n%2 == 0:
    s = n/2
    print s*m
else:
    s = (n-1)/2
    cnt = s*m
    p = (m-1)/2
    cnt += p
    print cnt
  