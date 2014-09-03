#include <iostream>
/********** Brute Force String Search Start *****/
int brutesearch(string p, string a)
{
	int i, j, M = p.length(), N = a.length();
	for (i = 0, j = 0; j < M && i < N; i++, j++)
	{
		while (a[i] != p[j]) 
		{
			i -= j-1;
			j = 0;
		}
	}

	if (j == M) return i-M;
	else return i;
}
/********** Brute Force String Search End *****/


/*********** Kunth Morris Pratt Algorithm Start ***********/
int next[1000];

initnext(string p)
{
	int i, j, M = p.length();
	next[0] = -1;
	for (i = 0, j = -1; i < M; i++, j++, next[i] = (p[i] == p[j])? next[j]: j)
		while ((j >= 0) && (p[i] != p[j])) j = next[j];
}

int kmpsearch(string p, string a)
{
	int i, j, M = p.length(), N = a.length();
	initnext(p);
	for (i = 0, j = 0; j < M && i < N; i++, j++)
		while ((j >= 0) && (a[i] != p[j]))
			j = next[j];
	if (j == M)
		return i-M;
	else
		return i;
}
/*********** Kunth Morris Pratt Algorithm End ***********/

/************ Boyer Moore Algorithm Start *******/
int skip[10000];

initskip(int p)
{

}

int mischarsearch(string p, string a)
{
	int i, j, t, M = p.length(), N = a.length();
	initskip(p);
	for (i = M-1, j = M-1; j > 0; i--, j--)
		while (a[i] != p[j])
		{
			t = skip[index(a[i])];
			i += (M-j > t) ? M-j: t;
			if (i >= N) return N;
			j = M-1;
		}
	return i;
}
/************ Boyer Moore Algorithm End *********/

/************ Rabin-karp Algorithm Start *******/
#define q 33554393
#define d 32

int rksearch(string p, string a)
{
	int i, dM = 1, h1 = 0, h2 = 0;
	int M = p.length(), N = a.length();

	for (i = 1; i < M; i++)
		dM = (d * dM) %q;
	for (i = 0; i < M; i++)
	{
		h1 = (h1*d+index(p[i])) % q;
		h2 = (h2*d+index(a[i])) % q;
	}

	for (i = 0; h1 != h2; i++)
	{
		h2 = (h2+d*q-index(a[i])*dM) % q;
		h2 = (h2*d+index(a[i+M])) % q;
		if (i > N-M) return N;
	}

	return i;
}
/************ Rabin-karp Algorithm End *******/