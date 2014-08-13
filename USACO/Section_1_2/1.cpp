/*
ID: vinod.d1
PROB: milk2
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

struct timespan{
 int start, end;
 bool operator < (const timespan &t) const{
  return start < t.start;
 }
};

int main() {
	ofstream fout ("milk2.out");
	ifstream fin ("milk2.in");

	int t, j, st, end, longestm=0, longestnm=0;
	vector<timespan> actives;

	fin >> t;

	for (j=0;j<t;j++) {
		fin >> st;
		fin >> end;
		timespan new_timespan;
		new_timespan.start = st;
		new_timespan.end = end;
		actives.push_back(new_timespan);
	}

	 // remove overlap
    sort(actives.begin(), actives.end());

    vector<timespan>::size_type i = 0;

	while (i < actives.size()) {
		int rng = actives[i].end;
		int lsv = actives[i].end;
		st = actives[i].start;
		i++;
		while (i  < actives.size() && actives[i].start <= rng) {
			if (rng < actives[i].end)
				rng = actives[i].end;
			lsv = actives[i].end;
			i++;
		}

		if (i  < actives.size()) {
			int v = (actives[i].start - rng);
			if (v > longestnm)
				longestnm = v;
		}

		if (longestm < (rng-st)) {
			longestm = (rng-st);		
		}
	}

	fout << longestm << " " << longestnm << "\n";

	return 0;
}