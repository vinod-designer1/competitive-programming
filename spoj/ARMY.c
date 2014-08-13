#include <stdio.h>

int main() {
	int t;
	scanf("%d", &t);

	while (t-- > 0) {
		int i;

		int ar1L = 0;
		int ar2L = 0;
		scanf("%d %d", &ar1L, &ar2L);

		int maxar1 = -1;
		int maxar2 = -1;

		for (i = 0; i < ar1L; i++){
			int num;
			scanf("%d", &num);
			if (num > maxar1){
				maxar1 = num;
			}
		} 

		for (i = 0; i < ar2L; i++){
			int num;
			scanf("%d", &num);
			if (num > maxar2){
				maxar2 = num;
			}
		} 

		if (maxar2 > maxar1) {
			printf("%s\n","MechaGodzilla");
		} else {
			printf("%s\n","Godzilla");
		}
	}

	return 0;
}