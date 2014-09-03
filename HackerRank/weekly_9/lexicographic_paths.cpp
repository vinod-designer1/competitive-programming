using namespace std;
#include <bits/stdc++.h>

// no of paths from 0,0 to x,y in c(x+y, y)

long long int f(long long int a, long long int b) // to calucalte (a+b)!/a!b!
{
    long long int res = 1;
    long long int i = 1;
    for(i=1 ; i<= (a+b) ; i++)
        res = res*i;
    for(i=1 ; i<= a ; i++)
        res = res/i;
    for(i=1 ; i<= b ; i++)
        res = res/i;
    return res;
}

void solve(long long int n, long long int m, long long int k)
{
	if (n == 0 && m == 0)
		return;
	else if (n == 0)
	{
		m--;
		cout << "V";
		solve(n, m, k);
	} else if (m == 0)
	{
		n--;
		cout << "H";
		solve(n, m, k);
	} else {
		if (f(n-1, m) > k)
		{
			cout << "H";
			solve(n-1, m, k);
		} else{
			cout << "V";
			solve(n, m-1, k-f(n-1, m));
		}
	}
}

int main()
{
	int t, x, y, k, i;

	cin >> t;
	while (t--)
	{
		cin >> x >> y >> k;
		solve(x, y, k);
		cout << endl;
	}
}