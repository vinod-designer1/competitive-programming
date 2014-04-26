#http://en.wikipedia.org/wiki/Fibonacci_number
def multiply(F, M):
	x =  F[0][0]*M[0][0] + F[0][1]*M[1][0]
	y =  F[0][0]*M[0][1] + F[0][1]*M[1][1]
	z =  F[1][0]*M[0][0] + F[1][1]*M[1][0]
	w =  F[1][0]*M[0][1] + F[1][1]*M[1][1]

	F[0][0] = x
	F[0][1] = y
	F[1][0] = z
	F[1][1] = w

def power_n_matrix(F, powr):
	M = [[1,1],[1,0]]
	power_n_matrix(F, powr/2);
	multiply(F, F);

	if (powr%2 != 0):
		multiply(F, M)

def fib(n):
	F = [[1,1],[1,0]]
	if (n == 0):
		return 0
	power_n_matrix(F, n-1)

	return F[0][0]

