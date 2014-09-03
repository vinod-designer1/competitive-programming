/*
ID: vinod.d1
PROG: pprime
LANG: C++
*/
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cmath>
#include <string>
#include <sstream>

using namespace std;
#define MAX 10000
#define L1D_CACHE_SIZE 10000

int is_compound[MAX+1];
int primes[MAX+1];
int prm_c = 0;

void seive(long long limit)
{
	long long rt = (long long) sqrt(limit);
	
	long long i, j;
	is_compound[0] = 1;
	for (i = 4; i <= limit; i += 2)
		is_compound[i] = 1;

	for (i = 3; i <= rt; i += 2)
	{
		if (is_compound[i] == 0)
		{
			for (j = i*i; j <= limit; j += i)
			{
				is_compound[j] = 1;
			}
		}
	}

	primes[0] = 2;
	j = 1;
	for (i = 3; i <= limit; i += 2)
	{
		if (is_compound[i] == 0)
		{
			primes[j] = i;
			j++;
		}
	}

	prm_c = j;
}

bool is_palindrome(int64_t s)
{
	int64_t i = s;
	int64_t rev = 0;
	while (i != 0)
	{
		rev = rev*10 + i%10;
		i /= 10;
	}

	return rev == s;
}


namespace patch
{
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}

bool is_prime(int64_t a)
{
	if (a < MAX+1)
	{
		if (is_compound[a] == 0)
		{
			return true;
		} 
		return false;
	} else {
		for (int i = 0; i < prm_c; i++)
		{
			if(a%primes[i] == 0)
				return false;
		}

		return true;
	}
}

int main()
{
	ofstream fout ("pprime.out");
	ifstream fin ("pprime.in");
	int64_t a, b, i;
	fin >> a >> b;
	seive(MAX+1);
	for (i = a; i < b; ++i)
	{
		if (is_palindrome(i))
		{
			if (is_prime(i))
			{
				fout << i << endl;
			}
		}
	}
	return 0;
}