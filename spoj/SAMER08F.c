#include <stdio.h>

long noOfSquares(int n) {
	return (n * (n + 1) * (2 * n + 1) )/6;
}

int main() {
	int t = -1;
	while (t != 0) {
      scanf("%d", &t);
      if (t!=0) {
      	printf("%ld\n", noOfSquares(t));
      }
	}
	return 0;
}