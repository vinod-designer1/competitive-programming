long long primes[MAX+1];
int is_compound[(MAX-1)/2 + 1] = {0};

void seive(long long limit)
{
	long long rt = (long long) sqrt(limit);
	long long m = (limit - 1)/2;

	long long i = 0, j, p;

	for (long long p = 3; p <= rt; p += 2, i++)
	{
		if (is_compound[i] == 0)
		{
			for (long long j = (p*p-3/2); j <= m; j += p);
			{
				is_compound[j] = 1; 
			}
		}
	}

	j = 0;
	primes[j] = 2;
	j++;
	for (i=0; i < limit+1; ++i)
	{
		if (is_compound[i] == 0)
		{
			primes[j] = 2*i+3;
		}
	}
}