#include <cstdio>

using namespace std;

int val[1000001];
int mulp(int n, int c, int p)
{
	int i, j, k, res = 1, z = p+1;
	for (i=z,j=0;i<=n;i++, j++) {
		val[j] = i;
	}

	for (i=c;i>=2;i--) {
		k = 0;
		j = (z/i);
		if (z % i != 0)
			j += 1;
		k += (i*j - z);
		while(val[k]%i != 0 && k <= n) {
			k += i;
		}
		val[k] = (val[k]/i);
	}

	for (i=0;i<(n-p);i++)
	{  
        res *= val[i];
	}

	return res;
}

int comb(int n, int c)
{
	if (c == 0 or c == n) {
		return 1;
	} else {
        if (c > (n-c)) {
            return mulp(n, (n-c), c);
        } else {
            return mulp(n, (c), (n-c));
        }
	}
}

int prob(int n, int k)
{
	int limit = (k-n)/6,i, on = 1, j, perc;
	long double pv;
	long long int sumv = 0;

	for (i=0;i<=limit;i++)
	{
		if (i%2 == 1)
			on = -1;
		else
			on = 1;
		j = k - 6*i - 1;
        sumv += (on) * (comb(n,i)) * (comb(j, (n-1)));
	}

	sumv *= 100;
	pv = sumv;

	for (i=0;i<n;i++)
		pv /= (6.0);

	perc = (pv);

	return perc;
}

int main()
{
	int t, n, k;
	scanf("%d",&t);

	while(t-->0)
	{
		scanf("%d %d", &n, &k);
		printf("%d\n", prob(n, k));
	}

	return 0;
}