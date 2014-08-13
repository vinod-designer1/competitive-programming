#include <cstdio>
#include <algorithm>

using namespace std;

int v[2000];
int ar[2000][2000];

int main()
{
    int n, i, a,  j;
    
    scanf("%d", &n);
    for (i=0; i < n; i++)
    {
    	scanf("%d", &v[i]);
    	ar[i][i] = n * v[i];
    }

    for(int i=n-2;i>=0;--i){
		for(int j=i+1;j<n;++j){
			a=n-j+i;
			ar[i][j]=max(ar[i+1][j]+(a)*v[i] , ar[i][j-1]+(a)*v[j]);
		}
	}

	prtinf("%d\n", ar[0][n-1]);

    return 0;
}