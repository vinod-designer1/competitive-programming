#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#define MAX 10000001

int main()
{
	long int n;
	scanf("%ld", &n);
	long int ar[n], car[1000001], fact[1000001], maxv=-1;
	for(long int i=0;i<n;i++) {
		scanf("%ld", &ar[i]);
		if maxv < ar[i]:
			maxv = ar[i];
		car[ar[i]]++;
	}
	for (long int i=0;i<n;i++) {
		if (ar[i] > 1) {
			for (long int j=ar[i];j<=maxv;j+=ar[i])
				fact[j] += car[i];
			car[i] = 0;
		}
	}
	for (long int i = 0; i < n; ++i)
	{
		printf("%ld\n", (fact[i]-1+car[1]));
	}
	return 0;
}