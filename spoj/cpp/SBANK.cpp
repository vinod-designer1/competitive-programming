#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int main()
{
	int t, n, I, J;
	char account_no[40];
	map<string, int> accounts;
	map<string, int>::iterator iter;

	scanf("%d", &t);

	while (t--) {
		scanf("%d\n", &n);
		accounts.clear();
		for (I=0; I < n; ++I) {
			gets(account_no);
			accounts[(string)account_no]++;
		}
		for (iter = accounts.begin(); iter != accounts.end(); ++iter) {
		   printf("%s %d\n", iter->first.c_str(), iter->second);
	    }
	    printf("\n");
	}

	
	return 0;
}