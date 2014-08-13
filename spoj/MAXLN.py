##max of eq id d(F(x))/dx = 0
def maxOfS(r):
	return (4 * r * r + 0.25)

t = input()
i = 1
while t > 0:
	ans = maxOfS(input())
	print 'Case',str(i) + ':','%.2f'%ans

	i += 1
	t -= 1