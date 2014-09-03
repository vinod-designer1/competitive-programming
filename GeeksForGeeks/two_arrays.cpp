#include <iostream>

using namespace std;

int bin_search(int a[], int val, int i, int j)
{
	int mid;

	while (i < j)
	{
		mid = (i+j)/2;
		cout << i << " " << j << endl;
		if (a[mid] < val)
		{
			i = mid+1;
		} else {
			j = mid-1;
		}
	}

	cout << i << " " << j << endl;

	return i;
}

int main()
{
	int ar1[] = {1, 3, 4, 5, 9};
	int ar2[] = {2, 4, 6, 8, 10};
}