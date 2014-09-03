#include <iostream>
#include <cstdio>
#include <queue>

using namespace std;

#define maxV 50

/******** Adjecency Matrix Start *******/
int j, x, y, V, E;
int a[maxV][maxV];
adjmatrix()
{
	scanf("%d %d\n", &V, &E);
	for (x = 1; x <= V; x++)
		for (y = 1; y <= V; y++)
			a[x][y] = 0;
	for (x = 1; x <= V; x++) a[x][x] = 1;
	for (j = 1; j <= E; j++)
	{
		scanf("%c %c\n", &v1, &v2);
		x = index(v1);
		y = index(v2);
		a[x][y] = 1;
		a[y][x] = 1;
	}
}
/******** Adjecency Matrix End ********/

/******** Adjecency List Start *******/
struct node
{
	int v;
	struct node *next;
};

int j, x, y, V, E;
struct node *t, *z;
struct node *adj[maxV];
adjlist()
{
	scanf("%d %d\n", &V, &E);
	z = new node;
	z->next = z;
	for (j = 1; j <= E; j++)
		adj[j] = z;
	for (j = 1; j <= E; j++)
	{
		scanf("%c %c\n", &v1, &v2);
		x = index(v1);
		y = index(v2);
		t = new node;
		t->v = x;
		t->next = adj[y];
		adj[y] = t;
		t = new node;
		t->v = y;
		t->next = adj[x];
		adj[x] = t;
	}
}
/******** Adjecency List End ********/

/******** Depth First Search Start ******/
int val[maxV];
int id = 0;
queue<int> bfs;
visit(int k)
{
	struct node *t;
	val[k] = ++id;
	for (t = adj[k]; t != z; t = t->next)
		if (val[t->v] == 0) visit(t->v);
}

listdfs()
{
	int k;
	for (k = 1; k <= V; k++) val[k] = 0;
	for (k = 1; k <= V; k++)
		if (val[k] == 0) visit(k);
}
/******** Depth First Search End ******/

/********* Breadth First Search Start ********/
int val[maxV];
int id = 0;
visit (int k)
{
	struct node *t;
	bfs.put(k);
	while (!bfs.is_empty())
	{
		k = bfs.get();
		val[k] = ++id;
		for (t = adj[k]; t != z; t = t->next)
			if (val[t->v] == 0)
			{
				bfs.put(t->v);
				val[t->v] = -1;
			}
	}
}

listbfs()
{
	int k;
	for (k = 1; k <= V; k++) val[k] = 0;
	for (k = 1; k <= V; k++)
		if (val[k] == 0) visit(k);
}
/********* Breadth First Search End **********/

/********* Biconnected graph Start *********/
// changes to visit procedure for dfs
int visit(int k)
{
	struct node *t;
	int m, min;
	val[k] = ++id;
	min = id;
	for (t = adj[k]; t != z; t = t->next)
	{
		if (val[t->v] == 0)
		{
			m = visit(t->v);
			if (m < min) min = m;
			if (m >= val[k]) printf("%c", name(k));
		}
		else if (val[t->v] < min) min = val[t->v];
	}
	return min;
}
/********* Biconnected graph End ***********/


/********* Union-Find Algorithm Start ************/

/********* Union-Find Algorithm End ************/

/********* Minimum Spanning Tree Start **********/

/***** Priority First Search Start *****/
//@TODO
/***** Priority First Search End *****/

/***** Kruskal Start *****/
// select smallest edge first and make sure it doesn't form a cycle
//@TODO
/***** Kruskal End *****/
/********* Minimum Spanning Tree End **********/

/********** Shortest Path Start *********/

/********** Shortest Path End ***********/