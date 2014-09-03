#include <iostream>

using namespace std;

int main()
{
	int inch;
	bool is_possible;
	char first_char; // a byte
	double root_val;
	char v[10];
	char* p;
	p = &v[3]; // & apecifies address
	cout << "Hello, new world!\n";

	switch (first_char) {
	case 'y':
		cout << "yes";
	default:
		cout << "no";
	}
}