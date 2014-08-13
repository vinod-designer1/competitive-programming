/*
ID: vinod.d1
PROB: ride
LANG: C++
*/
#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ofstream fout ("ride.out");
	ifstream fin ("ride.in");
	string comet, group;
	fin >> comet;
	fin >> group;
	int comet_v = 1, group_v = 1, i;

	for (i = 0;i < comet.length(); i++) {
		comet_v = (comet_v * (comet[i] - 'A' + 1))%47;
	}

	for (i = 0;i < group.length(); i++) {
		group_v = (group_v * (group[i] - 'A' + 1))%47;
	}

	if (comet_v == group_v) {
		fout << "GO" << "\n";
	} else {
		fout << "STAY" << "\n";
	}

	return 0;
}