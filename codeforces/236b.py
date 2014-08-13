a,b,c = map(int, raw_input().split())

facts = [0]*((a*b*c)+1)

for i in range(1, (a*b*c)+1):
	for j in range(i, (a*b*c)+1, i):
		facts[j] += 1

sm = 0
for i in range(1, a+1):
	for j in range(1, b+1):
		for k in range(1, c+1):
			sm += facts[i*j*k]
print sm%1073741824