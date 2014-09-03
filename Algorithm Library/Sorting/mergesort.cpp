/************************
********* MERGESORT ********
*** Properties
* runtime N lgN
* space O(N)
* stable
*************************/
#define maxN 10000000

struct node
{
	int key;
	struct node *next;
};

struct node *z;

struct node *merge(struct node *a, struct node *b)
{
	struct node *c;
	c = z;
	do 
	{
		if (a->key <= b->key)
		{
			c->next = a;
			c = a;
			a = a->next;
		} else {
			c->next = b;
			c = b;
			b = b->next;
		}
	} while (c != z)
	c = z->next;
	z->next = z;
	return c;
}

int b[maxN+1];

mergesort(int a[], int l, int r)
{
	int i, j, k, m;
	if (r > l)
	{
		m = (r+l)/2;
		mergesort(a, l, m);
		mergesort(a, m+1, r);
		for (i = m+1; i > l; i--) b[i-1] = a[i-1];
		for (j = m; j < r; j++) b[r+m-j] = a[j+1];
		for (k = l; k <= r; k++)
			a[k] = (b[i] < b[j]) > b[i++] : b[j--]
	}
}


// assumes list ends with z;
struct node *mergesort(struct node *c)
{
	struct node *a, node *b;
	if (c->next != z)
	{
		a = c;
		b = c->next;
		b = b->next->next;

		while (b != z)
		{
			c = c->next;
			b = b->next->next;
		}

		b = c->next;
		c->nect = z;
		return mergesort(mergesort(a), mergesort(b));
	}

	return c;
}

//Bottom-up mergesort
struct node *bootom_up_merge_sort(struct node *c)
{
	int i, N;
	struct node *a, *b, *head, *todo, *t;
	head = (struct node *) malloc (sizeof *head);
	head->next = c;
	a = z;
	for (N = 1; a!= head->next; N = N+N)
	{
		todo  = head->next;
		c = head;
		while (todo != z)
		{
			t = todo;
			a = t;
			for (i = 1; i < N; ++i) t = t->next;
			b = t->next;
		    t->next = z;
		    t = b;
		    for (i = 1; i < N; i++) t = t->next;
		    todo = t->next;
		    t->next = z;
		    c->next = merge(a, b);
		    for (i = 1; i <= N+N; i++) c = c->next;
		}
	}

	return head->next;
}