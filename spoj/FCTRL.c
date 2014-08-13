#include<stdio.h>
long trailing_zeros_fact(long n) {
	long five_cnt = 0;
	long  i = 5; 

	while (i <= n) {
		five_cnt += (n/i);
		i *= 5;
	}

	return five_cnt;
}

int main() {
	int t;
	long n;
	scanf("%d", &t);
	while(t > 0) {
		scanf("%ld", &n);
		printf("%ld\n", trailing_zeros_fact(n));
		t -= 1;
	}
	return 0;
}