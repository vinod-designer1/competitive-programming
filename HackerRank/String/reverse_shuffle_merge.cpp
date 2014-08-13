#include <cstdio>
#include <iostream>

using namespace std;

string reverse(string a, int al) {
	string b = "";
	int i;
	for (i=al-1;i>=0;i--)
		b += a[i];
	return b;
}

int isValid(int ar[], string a)
{
    
}

string lexi_samll_string(string a)
{
	int al = a.length(), ar[26], i;
	string b = reverse(a);

	for (i=0; i < sl; i++) {
		ar[sl[i] - 'a']++;
	}

	for (i=0;i<26;i++) {
		ar[i] /= 2;
	}
}

int main()
{
	string a;
	cin >> a;
}