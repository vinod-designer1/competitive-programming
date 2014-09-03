#include "stdc++.h"
#include <algorithm>
using namespace std;
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

// 1
// 9907
// 9946
// 1
// 9969
// 9918
// 9973
// 1
// 9935
// 1

int main()
{
	int t, n, i, min_len = 100000, count = 0;
	i64 tmp, prev;
	vector<i64> skill;
	map <i64, priority_queue<int, vi, greater<int> > > team;
    ifstream fd ("team_formation_test_2", ifstream::in);
    fd >> t;
	while (t--)
	{
		skill.clear();
		team.clear();
		min_len = 100000;
		fd >> n;
		if (n < 1) {
			printf("%d\n", n);
			continue;
		}
		for (i = 0; i < n; ++i)
		{
			fd >> tmp;
			skill.pb(tmp);
		}
		sort(all(skill));

		for (i = 0; i < n; ++i)
		{
			count = 0;
			auto it = team.find(skill[i]-1);
			if (it != team.end())
				if (it->yy.size())
				{
					count = it->yy.top();
					it->yy.pop();
				}
			count++;
			team[skill[i]].push(count);
		}

		for (auto x: team)
			if (x.yy.size())
				min_len = min(min_len, x.yy.top());
		if( min_len >= INT_MAX ) min_len = 0;
		printf("%d\n", min_len);
	}
}