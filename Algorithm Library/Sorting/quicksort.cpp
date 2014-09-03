/*********************
******** QUICKSORT *********
*** Features
* In place (uses only a small auxiliary stack)
* on an average N log N operations
*** Draw Backs
* recursive (complicated if not recursive)
* pow(N,2) operations in the worstcase
* in-efficient on alrady sorted files
*** Describes As
* Divide-and-conquer
*** Working
* By partitioning a file into 2 parts, then sorting the parts independently
*** Facts
* it uses 2N lnN comparisons on the average
**********************/

#include <iostream>
#include <cstdio>

using namespace std;

void swap(int &a, int &b)
{
	int *t;
	t = a;
	a = b;
	b = t;
}

int partition(int a[], int l, int r)
{
	int pivot = (l+r)/2, 
	    i = l-1, 
	    j = r,
	    v = a[pivot];

	swap(a[r], a[pivot]);

	for (;;)
	{
		while(a[++i] < v)
		while(a[--j] > v)
		if (i >= j) break;
	    swap(a[i], a[j]);
	}

}

void quick_sort_rec(int a[], int l, int r)
{
	int i;
	if (r > l)
	{
		i = partition(a, l, r);
		quick_sort(a, l, i-1);
		quick_sort(a, i+1, r);
	}
}

void quick_sort_iter(int a[], int N)
{
	int i, l, r;
	l = 0; r = N-1;
	//stackinit();
	for (;;)
	{
		while (r  > l)
		{
			i = partition(a, l, r);
			if (i-1 > r-i)
			{
				//push(l);
				//push(i-1);
				l = i+1;
			} else {
				//push(i+1);
				//push(r);
				r = i-1;
			}
		}

		//if (stackempty()) break;
		//r = pop();
		//l = pop();
	}
}

int main()
{

}