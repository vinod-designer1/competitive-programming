/*
ID: vinod.d1
PROB: beads
LANG: C++
*/
#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main()
{
	ofstream fout ("beads.out");
	ifstream fin ("beads.in");

	int N, i, cnt=0, j, max=0, cl=0;
	string necklace;
	char p = ' ';

	fin >> N;
	fin >> necklace;
	necklace += necklace;

	for (i=1;i<N;i++) 
	{
		cnt = 0;
		cl = 0;
		j = i-1;

		while (j >= 0) {
			if (necklace[j]=='w') {
				cnt++;
			} else {
				if (cl == 0) { 
					cl++;
					p = necklace[j];
				}
				else {
					if (p != necklace[j])
						break;
				}
				cnt++;
			}
			j--;
		}

		cl = 0;
		int m = N+j+1;
		j = i;
		while (j < (m)) {
			if (necklace[j]=='w') {
				cnt++;
			} else {
				if (cl == 0) { 
					cl++;
					p = necklace[j];
				}
				else {
					if (p != necklace[j])
						break;
				}
				cnt++;
			}
			j++;
		}

		if (max < cnt) {
			max = cnt;
		}
	}

	fout << max << "\n";
	return 0;
}