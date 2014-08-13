#include <cstdio>
#include <iostream>
using namespace std;

int main()
{
    int a[26]={0}, b[26]={0}, t, sl, mid, i, cnt;
	string s;

	i = scanf("%d", &t);
	while (t-- > 0) 
	{
		for (i=0;i<26;i++) {
            a[i] = 0;
            b[i] = 0;
        }
		cnt = 0;

		cin >> s;
		sl = s.length();

		if (sl%2 == 0) {
			mid = sl/2;
			for (i=0;i<sl;i++) {
				if (i < mid) {
					a[s[i]-'a']++;
				} else {
					b[s[i]-'a']++;
				}
			}

			for (i=0;i<26;i++) {
				if (b[i] != 0) {
					if (a[i] < b[i]) {
						cnt += (b[i] - a[i]);
					}
				}
			}

			printf("%d", cnt);

		} else {
			printf ("-1");
		}
		printf("\n");
	}
    
    return 0;

}