/*
ID: vinod.d1
PROG: clocks
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
	ofstream fout ("clocks.out");
	ifstream fin ("clocks.in");

	int clocks[3][3], 
	    i, j, 
	    diff[3][3], 
	    noch=0, 
	    tmp,
	    frm[9],
	    cnt = 0; 
	    maxl = 0, maxind=-1, 
	    pos = 0;

	string stages = {
		'ABDE',
		'ABC',
		'BCEF',
		'ADG',
		'BDEFH',
		'CFI',
		'DEGH',
		'GHI',
		'EFHI'
	};

	for (i=0; i < 3; ++i)
	{
		for (j=0; j < 3; ++j) 
		{
			fin >> clocks[i][j];
			tmp = (12 - clocks[i][j])/3;
			if (tmp != 0)
				noch++;
			diff[i][j] = tmp;
	    }
	}

	while (noch !=0) {
		maxl = 0;
		maxind = -1;
		for (i=0; i < 9; ++i) 
		{
			string stg = stages[i];
			int slen = stg.length();
			pos = 1;
			for (j=0; j < slen; ++j) 
			{
				int r = (stg[j]-'A')/3;
				int c = (stg[j]-'A')%3;

				if (clocks[r][c] == 12) {
					pos = 0;
					break;
				}
			}

			if (pos == 1) {
				if (slen > maxl) {
					maxl = slen;
					maxind = (i+1);
				}
			}
		}

		string stg = stages[maxind - 1];

		frm[cnt] = maxind;
		cnt++;

		for (i=0; i < maxl; ++i)
		{
			int r = (stg[j]-'A')/3;
			int c = (stg[j]-'A')%3;

			clocks[r][c] += 3;

			if (clocks[r][c] == 12)
				noch--;
		}
	}

	for (i=0; i < cnt; ++i)
	{
		fout << frm[i] << " ";
	}

	return 0;
}