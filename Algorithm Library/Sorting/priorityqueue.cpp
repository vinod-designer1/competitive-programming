/***********************************
********* PRIORITY QUEUE *********
*** Implementation
* using queues and stacks
*** Applications
* simulation systems
* job scheduling
* numerical computations
*** operations which can be performed on priority queue
* construct N item priority queue
* insert new item
* remove the largest item
* replace the largest item with a new item (unless the new item is larger).
* change the priority of an item
* delete an arbitrary specified item.
* join two prioriy queues into a larger one.
*** Run times
* insert, remove, replace, delete, change 
  require less than 2 lgN with Heap
************************************/
#define maxN 100000
/****** Array Implementation ******/
static int a[maxN+1], N;

construct(int b[], int M)
{
	for (N = 0;N < M; N++)
		a[N] = b[N];
}

insert(int v)
{
	a[++N] = v;
}

int remove()
{
	int j, max, v;
	max = 0;
	for (j = 1; j < N; j++)
		if (a[j] > a[max]) max = j;
	v = a[max];
	a[max] = a[N--];
	return v;
}
/********* END Array Implementation ****/

/****** Heap Implementation ******/
upheap(int k)
{
	int v;
	v = a[k];
	a[0] = INT_MAX;

	while (a[k/2] <= v)
	{
		a[k] = a[k/2];
		k = k/2;
	}
	a[k] = v;
}

downheap(int k)
{
	int j, v;
	v = a[k];
	while (k <= N/2)
	{
		j = k+k;
		if (j < N && a[j] < a[j+1]) j++;
		if (v >= a[j]) break;
		a[k] = a[j];
		k = j;
	}
	a[k] = v;
}

int replace(int v)
{
	a[0] = v;
	downheap(0);
	return a[0];
}

int remove_heap()
{
	int v = a[1];
	a[1] = a[N--];
	downheap(1);
	return v;
}

insert_heap(int v)
{
	a[++N] = v;
	upheap(N);
}

/*********
** Heap sort 
* run time N logN with any input
* twice as slow as Quicksort on the average
** Idea
* buld heap for all elements
* remove one by one in order
**********/
void heap_sort(int b[], int N)
{
	int k;
	construct(b,0);
	for (k = 1; k <= N; k++) insert_heap(b[k-1]);
	for (k = N; k >= 1; k--) b[k] = remove_heap();
}

/************
*** Run Time
* Linear Time
* fewer than 2*N*lgN operations
*************/
void heap_sort_down(int b[], int N)
{
	int k, t;
	for (k = N/2; k >= 1; k--) downheap(a, N, k);
	while (N > 1)
	{
		t = a[1];
		a[1] = a[N];
		a[N] = t;
		downheap(a, --N, 1);
	}
}

int p[maxN+1], q[maxN+1];

pqdownheap(int a, int N, int k)
{
	int j,v;
	v = p[k];
	while(k <= N/2)
	{
		j = k+k;
		if (j < N && a[p[j]] < a[p[j+1]]) j++;
		if (a[v] >= a[p[j]]) break;
		p[k] = p[j];
		q[p[j]] = k;
		k = j;
	}
	p[k] = v;
	q[v] = k;
}

pqconstruct(int a[], int N)
{
	int k;
	for (k = 1; k <= N; k++)
	{
		p[k] = k;
		q[k] = k;
	}
	for (k = N/2; k >= 1; k--)
	{
		pqdownheap(a, N, k);
	}
}
/********* END Heap Implementation ****/