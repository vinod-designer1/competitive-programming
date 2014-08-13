k = input()
l = input()
m = input()
n = input()
d = input()

ar = [k,l,m,n]

dn = 0
for i in range(1,d+1):
	for j in ar:
		if i%j == 0:
			dn += 1
			break
print dn