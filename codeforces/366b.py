n,k = map(int, raw_input().split())
ar = map(int, raw_input().split())
minv = sum(ar)
minn = 0
for i in range(0, (k)):
	j = (i+k)%n
	sumv = ar[i]
	while j < n :
		sumv += ar[j]
		j = (j+k)
	if minv > sumv:
		minv = sumv
		minn = i
print (minn+1)