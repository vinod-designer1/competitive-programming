#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>

using namespace std;


int is_composite[1000001] = {0};
int no_coprimes[1000001] = {0};

void prime_sieve(int limit)
{
	int I = 0, J;
	is_composite[1] = 1;
	for (I=2; I < sqrt(limit)+1; ++I) {
		if (is_composite[I] == 0) {
			no_coprimes[I] = I-1;
			for (J = I*I;  J < limit; J = J+I) {
				is_composite[J] = 1;
				no_coprimes[J] -= (no_coprimes[J]/I);
			}
		}
	}
}

int euler_totient(int n)
{
	if (n > 1)
		return (no_coprimes[n] - no_coprimes[n]/n);
	else
		return (no_coprimes[n]);
}

int fi(int n) 
{ 
	int result = n; 
	for(int i=2;i*i <= n;i++) 
	{ 
	 if (n % i == 0) result -= result / i; 
	 while (n % i == 0) n /= i; 
	} 
	if (n > 1) result -= result / n; 
	return result; 
}

int main ()
{
	int I, t, n;

	for (I=0; I < 1000001; ++I)
		no_coprimes[I] = I;

	prime_sieve(1000000);

	scanf("%d", &t);

	while (t--)
	{
		scanf("%d", &n);
		printf("%d\n", fi(n));
	}

	return 0;
}