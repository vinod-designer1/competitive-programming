/*
ID: vinod.d1
PROG:  dualpal
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
 
using namespace std;

#include <sstream>
 
using namespace std;

template <typename T>
  string NumberToString ( T Number )
  {
     ostringstream ss;
     ss << Number;
     return ss.str();
  }

string convertBase(int N, int B)
{
	string res = "";
	char c = ' ';
	int q, r, s = 1;
	while (N != 0) {
		r = N%B;
		if ( r >= 10) {
		  c = ('A' + (r-10));
		} else {
		  c = (r) + '0';
		}
		N = N/B;
		res = c + res;
	}

	return res;
}

int isPalin(string s)
{
	int slen = s.length(), mid = slen/2, i;

	if (slen == 1)
		return 1;

	for (i=(mid-1); i>=0; --i)
	{
		if (s[i] != s[slen-i-1])
			return 0;
	}

	return 1;
}

int main()
{
	ofstream fout ("dualpal.out");
	ifstream fin ("dualpal.in");

	int N, S, i=0, cnt = 0, j, has=0;
	string cn;

	fin >> N >> S;

	i = S+1;

	while (cnt < N) 
	{
		has = 0;
		for (j=2; j<11; ++j) {
			cn = convertBase(i, j);
			if (isPalin(cn) == 1) {
				has++;
			}
			if (has >= 2)
				break;
		}

		if (has >= 2) {
			cnt++;
			fout << i << "\n";
		}
		i++;
	}

	return 0;
}