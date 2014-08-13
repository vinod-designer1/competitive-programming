/*
ID: vinod.d1
PROG:  palsquare
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
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

int main() {
	ofstream fout ("palsquare.out");
	ifstream fin ("palsquare.in");

	int B, i, is;
	string cn;	

	fin >> B;

	for (i=1; i < 300; ++i) 
	{
		is = i*i;
		cn = convertBase(is, B);
		if (isPalin(cn) == 1) {
			fout << convertBase(i, B) << " " << cn << "\n";
		}
	}

	return 0;
}