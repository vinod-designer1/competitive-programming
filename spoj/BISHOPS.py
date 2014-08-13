import sys
def noOfBishops(N):
	if N < 2:
		return N
	return (2 * N - 2)

for line in sys.stdin:
	print noOfBishops(int(line))