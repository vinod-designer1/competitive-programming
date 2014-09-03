using namespace std;
#include <bits/stdc++.h>

#define sgn(x,y) ((x)+eps<(y)?-1:((x)>eps+(y)?1:0))
#define rep(i,n) for(auto i=0; i<(n); i++)
#define mem(x,val) memset((x),(val),sizeof(x));
#define rite(x) freopen(x,"w",stdout);
#define read(x) freopen(x,"r",stdin);
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define sqr(x) ((x)*(x))
#define pb push_back
#define clr clear()
#define inf (1<<28)
#define ins insert
#define xx first
#define yy second
#define eps 1e-9

typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector < int > vi;
typedef vector < st > vs;
typedef map < int , int > mii;
typedef map < st , int > msi;
typedef set < int > si;
typedef set < st > ss;
typedef pair < int , int > pii;
typedef vector < pii > vpii;

#define valid(x,radious) ( sqr(x) + sqr( (i64)( sqrt( radious - sqr(x) ) ) ) == radious)

long long no_solutions(long long r, long long k)
{
	int a = 1, b = (int) sqrt(r);
	long long tmp, count = 0;

	while (a <= b)
	{
		if (valid(a, r))
			count++;
		a++;
	}

	count = (count)*4;

	if (count <= k)
		return true;
	return false;
}

int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	long long r, k;
	scanf("%d", &t);
	while (t--)
	{
		scanf("%lld %lld", &r, &k);
		if (no_solutions(r, k))
			printf("possible");
		else
			printf("impossible");
	

		printf("\n");
	}
	return 0;
}