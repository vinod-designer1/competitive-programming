#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

class BenfordsLaw {
   public:
   	int questionableDigit(int[], int);
};

int BenfordsLaw:: questionableDigit(int ar[], int a) {
	int s[9], i, ln;
	int arz = sizeof(ar) / sizeof(ar[0]);
	


	for (i = 0; i < 9; ++i)
	{
		s[i] = 0;
		expv[i] = (log(1+(1/((i+1)*1.0)))/log(10))*arz;
	}

	for (i=0;i<ar.size();i++) {
		int z = ar[i]/(pow(10, (int)(log(ar[i])/log(10))));
		s[z - 1]++;
	}

	for (i=0;i<9;i++) {
		if (s[i]/expv[i] >= a || expv[i]/s[i] >= a)
			return (i+1);
	}

	return -1;
}
