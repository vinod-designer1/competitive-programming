#include <stdio.h>
#include <string.h>

int anagrams(char *a, char *b, int st, int end){
    int c1[26] = {0};
	int c2[26] = {0};

	int nlen = end - st;

	int cnt = 0, i= 0;

	for (i = 0; i < nlen; i++) {
		c1[a[i] - 97] += 1;
	} 
		
	i = st;
	for (i = st; i < end; i++) {
		int ind = b[i] - 97;
		if (c1[ind] == 0) {
			return(0);
		}
		c2[ind] += 1;
	}

	for (i = 0; i < 26; i++) {
		if (c1[i] == c2[i]) {
			cnt += c1[i];
		}
	}

	if (cnt == nlen) {
		return(1);
	} else {
		return(0);
	}
}

int getUniqNum(char *a, int len) {
	int i=0, sum = 0;

	for (i = 0; i < len; i++) {
		sum += (a[i] - 97);
	}

	return(sum);
}


int main(int argc, char const *argv[])
{
	/* code */
	int k;
	char a[1000];
	char b[100000];

	scanf("%d", &k);

	int t,i;

	for (t = 0;t < k; t++) {
		scanf("%s", a);
		scanf("%s", b);

		int alen = strlen(a);
		int blen = strlen(b);

		int sums = getUniqNum(a, alen);

		int ex = 0;

		int sumn = 0;

		for (i = 0; i < (blen - alen + 1); i++) {
			if (i == 0) {
				int j = 0;

				for (j = 0; j < alen; j ++) {
					sumn += (b[j] - 97);
				}
			} else {
				sumn += (b[i+alen-1]) - (b[i-1]);
			}

			if (sumn == sums) {
				if (anagrams(a, b, i, (i+alen))) {
					ex = 1;
					break;
				}
			}
		}

		if (ex == 0) {
			printf("%s\n", "NO");
		} else {
			printf("%s\n", "YES");
		}
		
	}
	return 0;
}