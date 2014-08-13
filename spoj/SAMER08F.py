def noOfSquaresOnChessBoard(n):
	return (n * (n + 1) * (2 * n + 1) )/6

t = -1
while t != 0:
	t = input()
	if t!= 0:
		print noOfSquaresOnChessBoard(t)