#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>

//The quadrilateral with given side lengths that has the
// maximum area is the cyclic quadrilateral
//http://en.wikipedia.org/wiki/Brahmagupta%27s_formula
using namespace std;

double area_of_cyclic_quadrilateral(double a, double b, double c, double d)
{
	double s = (a+b+c+d)/2; //semi perimeter
	double area = (s-a) * (s-b) * (s-c) * (s-d);

	return sqrt(area);
}

int main()
{
	int t;
	double a, b, c, d;

	scanf("%d", &t);

	while (t--)
	{
		scanf("%lf", &a);
		scanf("%lf", &b);
		scanf("%lf", &c);
		scanf("%lf", &d);

		printf("%.2lf\n", area_of_cyclic_quadrilateral(a, b, c, d));
	}
	return 0;
}