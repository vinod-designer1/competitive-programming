#include <iostream>

#include "math.h"

using namespace std;

// Euler's Algorithm
int gcd(int u, int v)
{
	int t;

	while (u > 0)
	{
		if (u < v)
		{
			t = u;
			u = v;
			v = t;
		}
		u = u-v;
	}

	return v;
}

// N is base 10 number
string base10_to_B(int N, int B)
{
	string base_num = "";
	int tmp_remainder;
	char num_to_char;

	while (N > 0)
	{
		tmp_remainder = (N%B);
		if (tmp_remainder > 10) 
		{
			num_to_char = 'A' + (tmp_remainder-10);
		} else {
			num_to_char = tmp_remainder + '0';
		}

		base_num = num_to_char + base_num;

		N /= B;
	}

	return base_num;
}