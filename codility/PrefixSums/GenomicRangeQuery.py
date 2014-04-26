#https://codility.com/demo/take-sample-test/genomic_range_query
"""
A non-empty zero-indexed string S is given. String S consists of N characters from the set of upper-case English letters A, C, G, T.

This string actually represents a DNA sequence, and the upper-case letters represent single nucleotides.

You are also given non-empty zero-indexed arrays P and Q consisting of M integers. These arrays represent queries about minimal nucleotides. We represent the letters of string S as integers 1, 2, 3, 4 in arrays P and Q, where A = 1, C = 2, G = 3, T = 4, and we assume that A < C < G < T.

Query K requires you to find the minimal nucleotide from the range (P[K], Q[K]), 0 ≤ P[i] ≤ Q[i] < N.

For example, consider string S = GACACCATA and arrays P, Q such that:

    P[0] = 0    Q[0] = 8
    P[1] = 0    Q[1] = 2
    P[2] = 4    Q[2] = 5
    P[3] = 7    Q[3] = 7

The minimal nucleotides from these ranges are as follows:

        (0, 8) is A identified by 1,
        (0, 2) is A identified by 1,
        (4, 5) is C identified by 2,
        (7, 7) is T identified by 4.

Assume that the following declarations are given:

    struct Results {
      int * A;
      int M;
    }; 

Write a function:

    struct Results solution(char *S, int P[], int Q[], int M); 

that, given a non-empty zero-indexed string S consisting of N characters and two non-empty zero-indexed arrays P and Q consisting of M integers, returns an array consisting of M characters specifying the consecutive answers to all queries.

The sequence should be returned as:

        a Results structure (in C), or
        a vector of integers (in C++), or
        a Results record (in Pascal), or
        an array of integers (in any other programming language).

For example, given the string S = GACACCATA and arrays P, Q such that:

    P[0] = 0    Q[0] = 8
    P[1] = 0    Q[1] = 2
    P[2] = 4    Q[2] = 5
    P[3] = 7    Q[3] = 7

the function should return the values [1, 1, 2, 4], as explained above.

Assume that:

        N is an integer within the range [1..100,000];
        M is an integer within the range [1..50,000];
        each element of array P, Q is an integer within the range [0..N − 1];
        P[i] ≤ Q[i];
        string S consists only of upper-case English letters A, C, G, T.

Complexity:

        expected worst-case time complexity is O(N+M);
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

Strategy or Algo : Prefix Sum
"""

def findMinInRange(P, Q, S):
	prefix_ary = []

	len_s = 0
	for C in S:
		cr = [0]*4
		if (C == 'A'):
			cr[0] = 1
		elif (C == 'C'):
			cr[1] = 1
		elif (C == 'G'):
			cr[2] = 1
		elif (C == 'T'):
			cr[3] = 1

		prefix_ary.append(cr)
		len_s += 1

	j = 1
	while j < len_s:
		i = 0
		while i < 4:
			prefix_ary[i][j] += prefix_ary[j-1][i]
			i += 1
		j += 1

	len_q = len(P)
	i = 0
	result = []

	while i < len_q:
		x = P[i]
		y = Q[i]

		j = 0
		while j < 4:
			sub = 0
			if (x-1) > 0:
				sub = prefix_ary[x-1][j]
			if prefix_ary[y][j] - sub > 0:
				result.append(j+1)
				return
	return result







