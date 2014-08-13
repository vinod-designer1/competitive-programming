/*
ID: vinod.d1
PROG: barn1
LANG: C++
*/
#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
 
using namespace std;

int main() 
{
	ofstream fout ("barn1.out");
	ifstream fin ("barn1.in");

	int M, S, C, I, J, tmp, unused = 0;
	vector<int> stalls;
	vector<int> gaps;

	fin >> M >> S >> C;

	for (I=0;I<200;++I) {
		gaps.push_back(1);
	}

	for (I=0; I<C; ++I)
	{
		fin >> tmp;
		stalls.push_back(tmp);
	}

	sort(stalls.begin(), stalls.end());

	for (I=1; I < stalls.size(); ++I) {
		gaps[I-1] = ((stalls[I]-stalls[I-1]));
	}

	sort(gaps.begin(), gaps.end(), greater<int>());

	unused = stalls[0] + S - stalls[C-1] -1;

	for (I=0; I < M-1; ++I)
		unused = unused + gaps[I] - 1;

	fout << S - unused << "\n";

	return 0;
}

