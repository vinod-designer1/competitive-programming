#include <stdio.h>
#include <stdlib.h>

int closetMountains(int mt1[], int mt1L, int mt2[], int mt2L) {
	int i,j,minD = 100000000, tmp;
	for (i=0;i < mt1L;i++) {
		for (j=0;j < mt2L;j++){
			tmp = abs(mt1[i] - mt2[j]);
			if (tmp < minD) minD = tmp;
		}
	}

	return minD;
}

int main(int argc, char const *argv[])
{
	int t,mt1[1000], mt2[1000], mt1L, mt2L, i;
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &mt1L);
		for (i=0;i<mt1L;i++) {
			scanf("%d", &mt1[i]);
		}
		scanf("%d", &mt2L);
		for (i=0;i<mt2L;i++) {
			scanf("%d", &mt2[i]);
		}

		printf("%d\n", closetMountains(mt1, mt1L, mt2, mt2L));
	}
	return 0;
}