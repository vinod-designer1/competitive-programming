/*
ID: vinod.d1
PROG: milk3
LANG: C++
*/
#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ofstream fout ("milk3.out");
    ifstream fin ("milk3.in");
    int a, b, c;
    fin >> a >> b >> c;
    vector<int> sol;
    sol.push_back(c);

    if (c > a && b > a)
    {
    	sol.push_back(c-a);
    } 

    if (c > b)
    {
    	sol.push_back(c-b);
    	int i = a, j = b;
    	while ((c-b)+i < c  && i < j)
    	{
    		sol.push_back(c-b + i);
    		i += a;
    	}
    }

    if (c > a && (c-a) <= b)
    {
    	sol.push_back(a);
    }

    if (c > b && (c-b) <= a)
    {
    	if (a != b)
    		sol.push_back(b);
    }

    for (int i = 0; i < sol.size(); ++i)
    {
    	cout << sol[i] << " ";
    }
    return 0;
}