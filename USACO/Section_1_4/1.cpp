/*
ID: vinod.d1
PROG: packrec
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

struct rec{
 int x,y, ind;
};

bool recOpy (rec i,rec j) { return (i.y > j.y); }

bool recOpx (rec i,rec j) { return (i.x > j.x); }

int main()
{
	ofstream fout ("packrec.out");
	ifstream fin ("packrec.in");

	int t, x, y, i;
	vector<packrec> recs;

	for (i=0; i < 4; ++i)
	{
		fin >> x >> y;
		rec newRec;
		newRec.x = x;
		newRec.y = y;
		newRec.push_back(newRec);
	}


}