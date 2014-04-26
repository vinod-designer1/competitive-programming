#http://en.wikipedia.org/wiki/Tur%C3%A1n%27s_theorem
#https://gist.github.com/yuvipanda/1285180
#Turan's theorem gives us an upper bound on the number of edges a graph can have if we wish that it should not have a clique of size x. 
#Though the bound is not exact, it is easy to extend the statement of the theorem to get an exact bound in terms of n and x. 
#Once this is done, we can binary search for the largest x such that f(n,x) <= m. 
#See: http://en.wikipedia.org/wiki/Tur%C3%A1n's_theorem
#http://en.wikipedia.org/wiki/Clique_%28graph_theory%29

def maxEdgesForClique(n,k):
	g1 = n%k
	g2 = k - g1
	sz1 = n/k + 1
	sz2 = n/k
	ret = (g1 * sz1 * g2 * sz2) + (g1 * (g1-1) * sz1 * sz1/2) + (g2 * (g2-1) * sz2 * sz2/2)
	return ret

def binarySearchVert(n, e):
	low = 1
	high = n+1
	while (low + 1 < high):
		mid = low + (high - low)/2
		k = maxEdgesForClique(n, mid)
		if k < e:
			low = mid
		else:
			high = mid
	return high

t = input()
while t > 0:
	ne = [int(i) for i in raw_input().strip().split(' ')]
	n = ne[0]
	e = ne[1]
	maxc = binarySearchVert(n, e)
	print maxc
	t -= 1
