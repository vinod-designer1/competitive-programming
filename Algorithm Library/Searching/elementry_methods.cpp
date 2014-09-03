/****************************
***
****************************/
#define maxN 100000;
/****** Sequential Search*******/
/******** linked list node start ******/
static struct node
{
	int key;
	int info;
};

static struct node a[maxN+1];
static int N;

seqinitialize()
{
	N = 0;
}

int seqsearch(int v)
{
	int x = N+1;
	a[0].key = v;
	a[0].info = -1;
	while (v != a[--x].key);
	return a[x].info;
}

seqinsert(int v, int info)
{
	a[++N].key = v;
	a[N].info = info;
}

/******** linked list node end ******/


/******** linked list start 2 ******/
static struct node
{
	int key;
	int info;
	struct node *next;
};
static struct node *head, *z;
listinitialize()
{
	head = (struct node *) malloc(sizeof *head);
	z = (struct node *) malloc(sizeof *z);
	head->next = z;
	z->next = z;
	z->info = -1;
}

int listsearch(int v)
{
	struct node *t = head;
	z->key = v;
	while (v > t->key) t = t->next;
	if (v != t->key) return z->info;
	return t->info;
}

listinsert(int v, int info)
{
	struct node *x, *t = head;
	z->key = v;
	while (v > t->next->key) t = t->next;
	x = (struct node *) malloc(sizeof *x);
	x->next = t->next;
	t->next = x;
	x->key = v;
	x->info = info;
}
/******** linked list end 2 ******/
/****** Sequential Search End *******/

/***** Binary Search *****/
/***
* logN+1 comparisons
***/
int a[maxN+1];
int binarysearch(int v)
{
	int l = 1;
	int r = N;
	int x;
	while (r >= l)
	{
		x = (l+r)/2; 
		// interpolation search if keys are evenly distributed
		// x = l + (v-a[l].key) * (r-l)/(a[r].key-a[l].key)
		if (v < a[x].key) r = x-1;
		else l = x+1;
		if (a[x].key == v) return a[x].info;
	}

	return -1;
}

/****** Binary Search End **/

/****** Binary Tree Search ****/
static struct node
{
	int key, info;
	struct node *l, *r;
};

static struct node *t, *head, *z;

treeinitialize()
{
	z = (struct node *) malloc(sizeof *z);
	z->l = z;
	z->r = z;
	z->info = -1;
	head = (struct node *) malloc(sizeof *head);
	head->r = z;
	head->key = 0;
}

treeinsert(int v, int info)
{
	struct node *p, *x;
	p = head;
	x = head->r;
	while (x != z)
	{
		p = x;
		x = (v < x->key) ? x->l: x->r;
	}

	x = (struct node *) malloc(sizeof *x);
	x->key = v;
	x->info = info;
	x->l = z;
	x->r = z;
	if (v < p->key)
		p->l = x;
	else
		p->r = x;
}

treedelete(int v)
{
	struct node *c, *p, *x;
	z->key = v;
	p = head;
	x = head->r;
	while (v != x->key)
	{
		p = x;
		x = (v < x->key) ? x-l: x->r;
	}
	t = x;
	if (t->r == z)
		x = x->l;
	else if (t->r->l == z)
	{
		x = x->r;
		x->l = t->l;
	} else {
		c = x->r;
		while (c->l->l != z)
			c = c->l;
		x = c->l;
		c->l = x->r;
		x->l = t->l;
		x->r = t->r;
	}

	free(t);
	if (v < p->key)
		p->l = x;
	else
		p->r = x;
}

int treesearch(int v)
{
	struct node *x = head->r;
	z->key = v;
	while (v != x->key)
		x = (v < x->key)? x->l: x->r;
	return x->info;
}
/****** Binary Tree Search End ***/