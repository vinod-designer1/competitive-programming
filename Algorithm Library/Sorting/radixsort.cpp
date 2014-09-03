/***********************
******** RADIX SORT *********
** Operations used
* >> shift
* & and operator
* zero all but j rightmost bits of x == x & ~(~0<<j) here ~(~0<<j) is a mask with ones
** Worst case
* most of keys are equal
** Properties
* N lgN avg comparisions
** Linear Sort
* stright raidx sort makes b/m passes
* m = b/4 is reasonable choice
* start ar b/(2*m)
************************/

void swap(int &a, int &b)
{
	int *t;
	t = a;
	a = b;
	b = t;
}

unsigned bits(unsigned x, int k, int j)
{
	return (x >> k) & ~(~0 << j); // (x div pow(2, k)) mod pow(2, j)
}

void straightradix(int a[], int b[], int N)
{
	// come from right to left
	int i, j, pass, count[M-1]; //M = pow(2,m)
	for (pass = 0; pass < (w/m)-1; pass++) //works if w is a multiple of m
	{
		for (j = 0; j < M; j++) count[j] = 0;
		for (i = 1; i < N; i++)
			count[bits(a[i], pass*m, m)]++;
		for (j = 0; j < M; j++)
			count[j] = count[j-1] + count[j];
		for (i = N-1; i >= 0; i--)
			b[count[bits(a[i], pass*m, m)]--] = a[i];
		for (i = 0; i < N; i++) a[i] = b[i];
 	}
}

void radix_exchange(int a[], int l, int r, int b)
{
	// Sort list by left most bit
	// first by b bit then by b-1 and soon
	int t, i, j;

	if ( r > l && b >= 0)
	{
		i = l;
		j = r;

		while (j != i)
		{
			while (bits(a[i], b, 1) == 0 && i < j) i++;
			while (bits(a[i], b, 1) != 0 && j > i) j--;
			swap(a[i], a[j]);
		}

		if (bits(a[r], b, 1) == 0) j++;
		radix_exchange(a, l, j-1, b-1);
		radix_exchange(a, j, r, b-1);
	}
}