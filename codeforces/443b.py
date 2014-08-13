s,k='aaabbbb',2
n, flag=len(s), 0
for l in range((n+k)/2,0,-1):
	print 'patt ', l
	for i in range(0, n+k-2*l+1):
		print 'pattin ', i, l
		if all(i + j + l >= n or s[i + j] == s[i + j + l] for j in range(l)):
			flag = 1; break
	if flag: break
print l*2