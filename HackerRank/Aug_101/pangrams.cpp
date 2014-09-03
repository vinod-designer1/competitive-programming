#include <iostream>
#include <cstdio>

using namespace std;

bool is_pangram(string s)
{
	int a[26] = {0};
	int i;

	for (i=0; i < s.length(); ++i)
	{
		if (s[i] >= 'a' && s[i] <= 'z')
			a[s[i]-'a']++;
		else if (s[i] >= 'A' && s[i] <= 'Z')
			a[s[i] - 'A']++;
	}

	for (i = 0; i < 26; ++i)
		if (a[i] == 0)
			return false;
	return true;
}

//scanf(" %[^\t\n]s",&str);
int main()
{
	string s;
	getline(cin, s);

	if (is_pangram(s))
		printf("pangram");
	else
		printf("not pangram");
}