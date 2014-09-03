/*
ID: vinod.d1
PROG: numtri
LANG: C++
*/
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{
	ofstream fout ("numtri.out");
	ifstream fin ("numtri.in");
	int n;
	int ar[500501] = {-1};
	int max_s = -1;
	fin >> n;
	for (int i = 1; i <= n; ++i)
	{
		for (int j = 0; j < i ; ++j)
		{
			fin >> ar[((i-1)*i)/2+j+1];
		}

		if (i > 1)
		{
			int st = ((i-1)*i)/2+1,
			    end = ((i+1)*i)/2,
			    prev_st = ((i-2)*(i-1))/2+1,
			    prev_end = st-1;
			for (int k = st; k <= end; ++k)
			{
				int prev_elm = prev_end - prev_st + 1;
				int a = -1, b = -1, c = -1;

				if (k-prev_elm-1 >= prev_st)
				{
					a = ar[k-prev_elm-1];
				}

				if (k-prev_elm >= prev_st && k-prev_elm <= prev_end)
				{
					b = ar[k-prev_elm];
				}

				ar[k] += max(a,b);
			}
		}
	}

	for (int i = ((n-1)*n)/2+1; i <= (((n+1)*n)/2); i++)
		if (max_s < ar[i])
			max_s = ar[i];
	fout << max_s << endl;
}
