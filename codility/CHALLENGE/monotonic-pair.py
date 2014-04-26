def solution(A):
	N = len(A)
	lmin = [0]*N
	rmax = [0]*N

	lmin[0] = A[0]
	i = 1
	while i < N:
		lmin[i] = min(A[i], lmin[i-1])
		i += 1

	rmax[N-1] = A[N-1]
	i = N-2
	while i >= 0:
		rmax[i] = max(A[i], rmax[i+1])
		i -= 1

	i = 0
	j = 0
	maxDiff = -1

	while j < N and i < N:
		if lmin[i] <= rmax[j]:
			maxDiff = max(maxDiff, j - i)
			j += 1
		else:
			i += 1

	if maxDiff == -1:
		maxDiff = 0
	return maxDiff

A = [2, 2, 2]
N = 6
print solution(A)

#https://codility.com/cert/view/certYNVUGN-SMNCG876Q4BDGUH7

