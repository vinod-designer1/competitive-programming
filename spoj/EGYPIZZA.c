#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[])
{
	int noQ = 0,
	noH = 0,
	noTF =0,
	num = 0,
	i = 0, N = 0, tP = 0;
	float cr;
	int n,d;
	scanf("%d", &N);

	while (N--) {
		scanf("%d/%d", &n, &d);
		cr = (n/(d*1.0));
		if (cr == 0.75){
			noTF += 1;
		} else if (cr == 0.25) {
			noQ += 1;
		} else {
			noH += 1;
		}
	}

	tP = noTF;
	noQ -= noTF;

	if (noH%2 == 0) {
		num = noH/2;
		tP += num;
	} else {
		num = noH/2;
		tP += num + 1;
		if (noQ > 0) {
			noQ -= 2;
		}
	}

	if (noQ > 0)
		tP += ceil(noQ/(4.0));

	printf("\n%d", (tP+1));
	return 0;
}