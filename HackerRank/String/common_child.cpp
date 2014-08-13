#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int ar[5001][5001];

int common_seq(string a, string b, int al, int bl)
{
	int i, j;
	// if (ar[al][bl] != 0)
	// 	return ar[al][bl];

	// if (al == 0 or bl == 0)
	// 	ar[al][bl] = 0;
	// else if (a[al-1] == b[bl-1])
	// 	ar[al][bl] = common_seq(a, b, al-1, bl-1)+1;
	// else
	// 	ar[al][bl] = max(common_seq(a, b, al-1, bl), common_seq(a, b, al, bl-1));

	for (i=1; i <= al; i++)
		for (j=1; j <= bl; j++) {
			if (a[i-1] == b[j-1])
				ar[i][j] = ar[i-1][j-1] + 1;
			else
				ar[i][j] = max(ar[i-1][j], ar[i][j-1]);
		}

	return ar[al][bl];
}

int main()
{
	int al, bl;
	string a, b;
	cin >> a;
	cin >> b;
	al = a.length();
	bl = b.length();
	printf("%d\n", common_seq(a, b, al, bl));
	return 0;
}