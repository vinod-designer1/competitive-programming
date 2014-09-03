using namespace std;
#include <bits/stdc++.h>

int main()
{
	int val = 0, i, t, n, x;
	cin >> t;
	while (t--)
	{
		cin >> n;
        val = 0;
		for (i = 0; i < n; ++i)
		{
			cin >> x;
			// no of times a integer appears is (i+1)*(N-i)
			// if N is even every integer appears even time so o
			// else if N is odd i should be even
			if (i%2 == 0)
				val ^= x;
		}

		if (n%2 == 0)
			cout << 0 << endl;
		else
			cout << val << endl;
	}
}