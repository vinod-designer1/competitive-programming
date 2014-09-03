/*
ID: vinod.d1
PROG: ariprog
LANG: C++
*/
#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

bool Sort(pair < int, int > a, pair < int, int > b)
{
	if (a.second < b.second)
		return true;
	if (a.second == b.second && a.first < b.first)
		return true;
	return false;
}

int main()
{
    ofstream fout ("ariprog.out");
    ifstream fin ("ariprog.in");
	int n, m, i, b, j, x, diff, k;
	bool ok;
	fin >> n;
	fin >> m;
	int bi[125001] = {0};
	pair < int, int > p;
	vector < pair < int, int > > answer;

	for (i = 0; i < 125001; ++i)
		bi[i] = -1;

	for (i = 0; i <= m; i++)
		for (j = i; j <=n; j++)
		{
			bi[i*i + j*j] = i*i + j*j;
		}

	for (i = 0; i < 125000; ++i)
	{
		b = bi[i];
		if (b == -1) continue;

		for (diff = ((125000 - i) / (n - 1)); diff > 0; --diff)
		{
			x = b;
			ok = true;
			for (k = 0; k < n; ++k)
			{
				x += diff;
				if (x > 125000 || bi[x] == -1)
				{
					ok = false;
					break;
				}
			}

			if (ok == true)
			{
				p.first = i;
				p.second = diff;
				answer.push_back(p);
			}
		}
	}

	sort(answer.begin(), answer.end(), Sort);
	if (answer.size() == 0)
		fout << "NONE" << endl;
	else
		for (i = 0; i < answer.size(); ++i)
		{
		    fout << answer[i].first << " " << answer[i].second << endl;
		}

	return 0;
}