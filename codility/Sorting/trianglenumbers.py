def isTriangleSet(x, y, z):
	if (x + y > z):
		if (y + z > x):
			if (x + z > y):
				return True
	return False

def binSearch(A, a_len, el):
	st = 0
	mid = a_len/2
	end = a_len
	ind = -1
	while (end-st)>0:
		mid = (end + st)/2
		if (A[mid] > el):
			end = mid
		elif (A[mid] < el):
			st = mid
		else:
			ind = mid
			break
	return ind


def triangleNUmbers(A):
	A.sort()
	a_len = len(A)
	j = a_len - 1
	while j >= 2:
		if A[j]+A[j-2] > A[j-1]:
			return 1
	return 0