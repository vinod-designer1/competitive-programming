#include <cstdio>
using namespace std;

#define PI 3.14159265358979323846264338327950

long double rad[10001];
int n;
int count(long double x)
{
    int cnt = 0,i;
    long double V;
    for (i=0;i<n;i++) {
    	V =  (PI * rad[i] * rad[i]);
    	cnt += (V/x);
    }
    return cnt;
}

int main()
{
	int t, frnds, i;
	long double high = -1, low=0, mid;
	scanf("%d", &t);
	while(t-- > 0)
	{
		low = 0;
		high = -1;
        scanf("%d %d", &n, &frnds);
        for (i=0;i<n;i++)
        {
        	scanf("%Lf", &rad[i]);
        	if (high < (PI * rad[i] * rad[i]))
        		high = (PI * rad[i] * rad[i]);
        }
        while((high - low)>1e-9)
        {
        	mid = (low+high)/(2.0);
        	if (count(mid) >= frnds+1)
        	{
               low = mid;
        	} else {
        		high = mid;
        	}
        }

        printf("%.4Lf\n",low);
	}
}