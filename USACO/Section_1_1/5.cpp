/*
ID: vinod.d1
PROB: friday
LANG: C++
*/
#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int dow(int y, int m, int d)
{
       static int t[] = {0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4};
       y -= m < 3;
       return (y + y/4 - y/100 + y/400 + t[m-1] + d) % 7;
}

int main() {
	ofstream fout ("friday.out");
	ifstream fin ("friday.in");
	int dc[7] = {0}, y=1900, N, i, j;
	fin >> N;

	for (i=0;i<N;i++)
	{
		for (j=1;j<=12;j++) 
		{
			dc[(dow(1900+i, j, 13)+1)%7]++;
		}
	}

	for (i=0;i<7;i++) {
		fout << dc[i];
		if (i!=6)
			fout << " ";
	}

	fout << "\n";

	return 0;
}