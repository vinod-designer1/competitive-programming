#include <iostream>
#include <cstdio>
#include <list>

using namespace std;

/********* 3.1 ***********/
/*****
(()(()))()
******/
bool is_properly_nested(string s)
{
	list<char> L;
	list<char>::const_iterator Li;
	int len_s = s.length(), i;

	for (i = 0; i < len_s; ++i)
	{
		if (s[i] == '(') {
			L.push_front('(');
		} else {
			Li = L.begin();
			if (*Li != '(')
				return false;
			L.pop_front();
		}
	}

	if (L.empty())
		return true;

	return false;
}
/********* 3.1E **********/

/********* 3.2 ***********/
/********* 3.2E **********/

/********* 3.3 ***********/
/********* 3.3E **********/

/********* 3.4 ***********/

/********* 3.4E **********/

int main()
{
	if (is_properly_nested("()()((())(())))"))
	{
		printf("ya man!!!");
	} else {
		printf("No bro!!");
	}
}