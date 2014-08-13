/*
ID: vinod.d1
PROG: namenum
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
 
using namespace std;

int main() {
	ofstream fout ("namenum.out");
	ifstream fin ("namenum.in");
	ifstream infile("dict.txt");

	int slen, i=0,has=0;
	long long t, num=0;
	string wrd;
	fin >> t;

	int ar[26] = {2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,0,7,7,8,8,8,9,9,9,0};

	while (infile >> wrd) {
		slen = wrd.length();
		num = 0;
		for (i=0; i < slen; ++i) 
		{
			num = num*10+(ar[wrd[i]-'A']);
		}

		if (num == t) {
			has = 1;
			fout << wrd << "\n";
		}
	}

	if (has == 0) 
	{
		fout << "NONE" << "\n";
	}

	return 0;
}