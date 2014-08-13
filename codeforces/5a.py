# n,m,k = map(int, raw_input().split())
# ar = map(int, raw_input().split())
# q = []
# for i in range(m):
# 	qry = map(int, raw_input().split())
# 	q.append(qry)

# for i in range(k):
# 	xy = map(int, raw_input().split())
# 	for j in range(xy[0]-1, xy[1]):
# 		qry = q[j]
# 		for p in range(qry[0]-1, qry[1]):
# 			ar[p] += qry[2]

# print ' '.join(map(str, ar))


R=lambda:map(int,raw_input().split())
n,m,k=R()
s=R()
u=[R() for _ in range(m)]
a,c,q=[0]*(m+1),0,[0]*(n+1)
print 'int ', u, s
for _ in range(k):
    x,y=R()
    a[x-1]+=1
    a[y]-=1
    print 'u ',a

for i in range(m):
    c+=a[i]
    d=u[i][2]*c
    q[u[i][0]-1]+=d
    q[u[i][1]]-=d
    print 's ', c, d, q, u
for i in range(n):
    q[i]+=[0,q[i-1]][i>0]
    s[i]+=q[i]
print " ".join(map(str,s))