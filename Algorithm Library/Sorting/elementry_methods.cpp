#include <cstdio>
#include <iostream>

using namespace std;

// sorting methods fro small methods
// and some special structures
// sorting method is stable if sorting preserves relative 
// order of equal keys in the file
// Example sorting grades of students where students
// name are arranged alphabetically if equal
// :: if records to be sorted are large, it is normally wise
//    to avoid shuffling them around by doing an "indirect sort":

void sort3(int a[], int N)
{
	// this function is actual
	// implementation of exchange operations
	// here we are exchange 1, 2, 3 elements
	// and ordering them increasing order
	int t;

	if (a[1] > a[2]) 
	{
		t = a[1];
		a[1] = a[2];
		a[2] = t;
	}

	if (a[1] > a[3])
	{
		t = a[1];
		a[1] = a[3];
		a[3] = t;
	}

	if (a[2] > a[3])
	{
		t = a[2];
		a[2] = a[3];
		a[3] = t;
 	}
}

void selection_sort(int a[], int N)
{
	// find minimum and replace with first element
	// left in the array
	// Time Complexity
	//   Search for min O(n) happens n times
	//   Replace with first available element O(1)
	//   Worst = O(n**2)
	//   Average = O(N*logN)
	// Space Complexity
	//   O(1) as no more than 4 varibles used
	// Application:
	//   insights: each item is moved once
	//   helps to sort files with very large records
	//   and small keys almost linear
	// uses N**2/2 comparisons and N exchanges

	int I, J, min_ind, t;

	for (I = 0; I < N; ++I) //runs N times
	{
		min_ind = I;
		for (J = I; J < N; ++J) //runs N-I times
		{
			if (a[min_ind] > a[J]) min_ind = J;
		}

		t = a[min_ind];
		a[min_ind] = a[I];
		a[I] = t;
	} // total time (N * (N+1))/2

}

void insertion_sort(int a[], int N)
{
	// Elements are inserted by moving large elements
	// one step right and insert element into vacated place
	// Time Complexity:
	//   Worst: O(N**2) reverse sorted
	//   if patilly this has very good run times
	// Space Complexity:
	//   O(1)
	// N**2/4 comparisons and N**2/8 exchanges avgcase and twice as many in worst case
	int I, J, v;

	for (I = 1; I < N; ++I)
	{
		J = I;
		v = a[I];
		while (J > 0 && a[J-1] > v)
		{
			a[J] = a[J-1];
			J--;
		}
		a[J] = v;
	}
}

void bubble_sort(int a[], int N)
{
	// exchange adjacent elemen if not in order
	// Time complexity
	//   O(N**2)
	// Space Complexity:
	//   O(1)
	// N**2/2 comparisons and N**2/2 exchanges avgcase and worst case
	int I, J, t;

	for (I = N-1; I >=0; --I)
		for (J = 1; J <= I; ++J)
		{
			if (a[J-1] > a[J]) 
			{
				t = a[J-1];
				a[J-1] = a[J];
				a[J] = t;
			}
		}
}

// Sorting Files with Large Records
// :: If array a[1]...a[N] consists of large records
//    then we prefer to manipulate an "index array" p[1]...p[N]
//    accessing original only for comparisons
//    if we define p[i] = i initially,
//    then algorithms above need only be modified to refer to a[p[i]] rather than a[i]
//    we can use a[i] for comparison
//    we sort and produce index array where p[1] is smallest
//    this avoides moving large records around excessively

void insertion_sort_large(int a[], int p[], int N)
{
	int I, J, v;
	for (I = 0; I < N; ++I) p[I] = I;

	for (I = 1; I < N; ++I)
	{
		v = p[I];
		J = I;
		while (a[p[J-1]] > a[v])
		{
			p[J] = p[J-1];
			J--;
		}
		p[J] = v;
	}
}

void insitu(int a[], int p[], int N)
{
	int I,J,k,t;

	for (I = 0; I < N; ++I)
		if (p[I] != I)
		{
			t = a[I];
			k = I;

			do
			{
				J = k;
				a[J] = a[p[J]];
				k = p[J];
				p[J] = J;
			} while (k != I);

			a[J] = t;
		}
}

void insertion (int a[], int *p[], int N)
{
	int I, J, *v;
	for (I = 0; I < N; ++I) p[I] = &a[I];

	for (I = 1; I < N; ++I)
	{
		v = p[I];
		J = I;
		while (*p[J-1] > *v)
		{
			p[J] = p[J-1];
			J--;
		}
		p[J] = v;
	}
}

// Insertion Sort is slow because it exchanges only
// adjacent elements
// it is an extension of insertion sort 
// which gain speed by allowing
// exchnages of elements that are far a part
// idea is to reaarrange the file taking helements
// h sorted files.

void shell_sort(int a[], int N)
{
	int i, j, h, v;
	for (h = 1; h < N/9; h = 3*h+1);
	for (; h > 0; h /= 3)
		for (i = h+1; i <= N ; ++i)
		{
			v = a[i];
			j = i;
			while (j >= h && a[j-h] > v)
			{
				a[j] = a[j-h];
				j -= h;
			}
			a[j] = v;
		}
}

int main()
{
	int a[] = {2, 4, 10, 7, 4, 6, 8, 1}, b[] = {2, 4, 10, 7, 4, 6, 8, 1}, c[] = {2, 4, 10, 7, 4, 6, 8, 1};
	int I;
	shell_sort(a, 8);
	printf(" Shell_Sort \n\n");
	for (I = 0; I < 8; ++I)
		printf ("%d ", a[I]);

	selection_sort(a, 8);
	bubble_sort(b, 8);
	insertion_sort(c, 8);

	printf(" Selection_Sort \n\n");
	for (I = 0; I < 8; ++I)
		printf ("%d ", a[I]);

	printf(" Bubble_Sort  \n\n");
	for (I = 0; I < 8; ++I)
		printf ("%d ", b[I]);

	printf("Insertion_Sort \n\n");
	for (I = 0; I < 8; ++I)
		printf ("%d ", c[I]);
	return 0;
}
