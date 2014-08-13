/*
ID: vinod.d1
PROG: milk
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

struct farmer{
 int price, quantity;
 bool operator < (const farmer &t) const{
  return price < t.price;
 }
};

int main()
{
	ofstream fout ("milk.out");
	ifstream fin ("milk.in");

	int milkq = 0, nofarm = 0, J, tmpC, tmpQ, quan=0, price = 0;
	vector<farmer> farmers;

	fin >> milkq >> nofarm;

	for (J = 0; J < nofarm; ++J)
	{
		fin >> tmpC >> tmpQ;
		farmer new_farmer;
		new_farmer.price = tmpC;
		new_farmer.quantity = tmpQ;
		farmers.push_back(new_farmer);
	}

	 // remove overlap
    sort(farmers.begin(), farmers.end());

    vector<farmer>::size_type I = 0;

    while (milkq > 0  && I < farmers.size())
    {
    	if (milkq >= farmers[I].quantity) {
    		milkq -= farmers[I].quantity;
    		price += farmers[I].price * farmers[I].quantity;
    	} else {
    		price += farmers[I].price * milkq;
    		milkq = 0;
    	}
    	I++;
    }

    fout << price << "\n";

    return 0;
}