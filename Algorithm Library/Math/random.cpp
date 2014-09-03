/********* Generating Random Numbers ********/
/**** Linear Congurent Method Start ***/
// p = 10**4*p1+p0 , q = 10**4*q1+q0
// (((p0*q1+p1*q0) % m1)*m1 + p0+q0) % 10**8
// ((a/m1)*r)/m1
#define m 100000000
#define m1 10000
#define b 31415821
static int a;

int mult(int p, int q)
{
	int p1, p0, q1, q0;
	p1 = p/m1;
	p0 = p%m1;

	q1 = q/m1;
	q0 = q%m1;

	return (((p0*q1+p1*q0) % m1)*m1 + p0*q0) % m;
}

int random()
{
	a = (mult(a,b)+1) % m;
	return a;
}
/**** Linear Congurent Method End ***/


/**** Addictive Congruential Method Start ****/
int b = 31, c = 55;
randinit(int s)
{
	for (a[0] = s, j = 0; j <= 54; j++)
		a[j] = (mult(a[j-1],b)+1)%m;
}

int randinit(int r)
{
	j = (j+1) % 55;
	a[j] = (a[(j+23) % 55] + a[(j+54) % 55]) % m;
	return ((a[j]/m1)*r)/m1;
}
/**** Addictive Congruential Method End ****/

// Randomness test
// chi-square = ∑0<=i<r (fi-N/r)**2/(N/r)
// closer to r the more random they are
int rmax = 10000;
float chisquare(int N, int r, int s)
{
	int i, j, f[rmax];
	for (i = 0; i < r; i++) f[i] = 0;
	for (i = 0; i < N; i++) f[randinit(r)]++;
	for (i = 0, t = 0; i < r; i++) t += f[i] * f[i];
	return (float) ((r*t/N) - N);
}
/********* Generating Random Numbers ********/