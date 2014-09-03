#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>

using namespace std;
map <int , long long> h;

long long max_dollars(int coins)
{
	if (h.count(coins) > 0)
		return h[coins];
	if (coins < 12)
		h[coins] = coins;
	else
		h[coins] = (max_dollars(coins/2) + max_dollars(coins/3) + max_dollars(coins/4));

	return h[coins];
}

int main() 
{
	int coins;

	while(scanf("%d", &coins) != EOF)
	{
		printf("%lld\n", max_dollars(coins));
	}
}