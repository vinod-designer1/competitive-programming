#include <iostream>
#include <cstdio>

using namespace std;

int string_diff(string a, string b, int S)
{
	int sl = a.length(), ml = 0, i, j, diff, st = 0, ln = 0;

	for (i=0;i<sl;i++)
	{
		j = 0;
		diff = 0;
		ln = 0;
		while (j < sl)
		{
			if (st == 1)
			{
				if (i+ln >= sl && diff < S) {
					diff += 2;
					ln += 2;
				}

			    printf("ct %d %d %d %d\n", i, j, ln, diff);
				if  (diff > S){
					st = 0;
					printf("ct in\n");
					if  (ml < (ln-1)) {
						ml = (ln-1);
					}
					diff = 0;
					ln = 0;
					continue;
				}

			   	if (b[i+ln] != a[j])
			   	{
			   		diff++;
			   	}
			   	ln++;
			}

			if (b[i] == a[j]) {
				st = 1;
				ln++;
			}
			j++;
		}

	}

	return ml;

}

int main()
{
	int t, s;
	string a, b;

	scanf("%d", &t);

	while(t-- > 0)
	{
		scanf("%d", &s);
		cin >> a;
		cin >> b;
		printf("%d\n", string_diff(b, a, s));
	}
}