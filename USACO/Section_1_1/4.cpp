/*
ID: vinod.d1
PROB: gift1
LANG: C++
*/
#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main() {
	ofstream fout ("gift1.out");
	ifstream fin ("gift1.in");
	int t, i, j, p, d, a;
	fin >> t;
	string tmp;
	map<string, int> nm;
	string s[t];

	for (i = 0; i < t; ++i)
	{
		fin >> tmp;
		nm[tmp] = 0;
		s[i] = tmp;
	}

	for (i = 0; i < t; ++i)
	{
		/* code */
		fin >> tmp;
		fin >> p >> d;
		if (d != 0) {
			a = p/d;
			nm[tmp] += (-p+(p%d));

			for (j = 0;j < d; ++j) 
			{
				fin >> tmp;
				nm[tmp] += a;
			}
		} else {
			nm[tmp] += p;
		}
	}

	for (i = 0;i < t;i++) 
	{
		fout << s[i] << " " << nm[s[i]] << "\n";
	}

	return 0;
}