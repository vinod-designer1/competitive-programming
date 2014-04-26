'''
Given an array A of N integers, we draw N discs in a 2D plane such that the I-th disc is centered on (0,I) and has a radius of A[I]. We say that the J-th disc and K-th disc intersect if J ≠ K and J-th and K-th discs have at least one common point.

Write a function:

    def solution(A) 

that, given an array A describing N discs as explained above, returns the number of pairs of intersecting discs. For example, given N=6 and:

    A[0] = 1  A[1] = 5  A[2] = 2 
    A[3] = 1  A[4] = 4  A[5] = 0  

intersecting discs appear in eleven pairs of elements:

        0 and 1,
        0 and 2,
        0 and 4,
        1 and 2,
        1 and 3,
        1 and 4,
        1 and 5,
        2 and 3,
        2 and 4,
        3 and 4,
        4 and 5.

so the function should return 11.

The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Assume that:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [0..2147483647].

Complexity:

        expected worst-case time complexity is O(N*log(N));
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

This is easy. Intiially we calculate all start and end points of discs. 
After go by all line and check count of discs inside current point. 
If in current point started some discs and intersection count increased by:
 already active distsc multiplied by count of started in current point (result += t * dps[i]) 
 and count of intersections of started(result += dps[i] * (dps[i] - 1) / 2) eg. 
 if started 5 discs in one of point it will increased by(1+2+3+4+5 intersections, 
 	or 5*(5-1) / 2[sum formula]).
'''
def Solution(A):
	a_len = len(A)
	dps = [0] * a_len
	dpe = [0] * a_len
	result = 0

	i = 0
	while i < a_len:
		dps[max(0, i-A[i])] += 1
		dpe[min(a_len - 1, i + A[i])] += 1

		i += 1

	j = 0 
	t = 0
	while j < a_len:
		if dps[j] > 0:
			result += t * dps[j]
			result += dps[j] * (dps[j] - 1) / 2
			t += dps[j]
		t -= dpe[j]
		j += 1
	return result