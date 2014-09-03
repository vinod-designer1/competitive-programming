#include <cstdio> 
#include <algotithm>

using namespace std;

#define Nmax 1000

struct point 
{
	int x, y;
	char c;
};

struct line 
{
	struct point p1, p2;
};

struct point polygon[Nmax];

int ccw (struct point p0,
	     struct point p1,
	     struct point p2)
{
	int dx1, dx2, dy1, dy2;
	dx1 = p1.x - p0.x;
	dy1 = p1.y - p0.y;
	dx2 = p2.x - p0.x;
	dy2 = p2.y - p0.y;
	if (dx1*dy2 > dy1*dx2) return 1;
	if (dx1*dy2 < dy1*dx2) return -1;
	if ((dx1*dx2 < 0) || (dy1*dy2 < 0)) return -1;
	if ((dx1*dx1+dy1*dy1) < (dx2*dx2+dy2*dy2)) return 1;
	return 0;
}

int intersect(struct line l1, struct line l2)
{
	return ((ccw(l1.p1, l1.p2, l2.p1)
		     * ccw(l1.p1, l1.p2, l2.p2)) <= 0)
	    && ((ccw(l2.p1, l2.p2, l1.p1)
		     * ccw(l2.p1, l2.p2, l1.p2)) <= 0)
}

float theta(struct point p1, struct point p2)
{
	int dx, dy, ax, ay;
	float t;
	dx = p2.x - p1.x;
	ax = abs(dx);
	dy = p2.y - p1.y;
	ay = abs(dy);
	t = (ax+ay == 0)? 0: (float) dy/(ax+ay);
	if (dx < 0)
		t = 2 - t;
	else if (dy < 0)
		t = 4 + t;
	return t * 90.0;
}

int inside(struct point t, struct point p[], int N)
{
	int i, count = 0,  j = 0;
	struct line lt, lp;
	p[0] = p[N];
	p[N+1] = p[1];
	lt.p1 = t;
	lt.p2 = t;
	lt.p2.x = INT_MAX:
	for (i = 1; i <= N; i++)
	{
		lp.p1 = p[i];
		lp.p2 = p[i];
		if (!intersect(lp, lt))
		{
			lp.p2 = p[j];
			j = i;
			if (intersect(lp, lt)) count++;
		}
	}
	return count & 1;
}

/****** Convex Hull Start *****************/
int wrap(struct point p[], int N)
{
	// worst case pow(N,2)
	// it can be generalized to 3 or more dimensions
	int i, min, M;
	float th, v;
	struct point t;
	for (min = 0, i = 1; i < N; i++)
		if (p[i].y < p[min].y) min = i;
	p[N] = p[min];
	th = 0.0;
	for (M = 0; M < N; M++)
	{
		t = p[M];
		p[M] = p[min];
		p[min] = t;
		min = N;
		v = th;
		th = 360.0;
		for (i = M+1; i <= N; i++)
		{
			if (theta(p[M], p[i]) > v)
				if (theta(p[M], p[i]) < th)
				{
					min = i;
					th = theta(p[M], p[min]);
				}
		}
		if  (min == N) return M;
	}
}

int grahamscan(struct point p[], int N)
{
	// after sort this run in linear time
	int i, min, M;
	struct point t;
	for (min = 1, i =2; i <= N; i++)
		if (p[i].y < p[min].y) min = i;
	for (i = 1; i <= N; i++)
		if (p[i].y == p[min].y)
			if (p[i].x > p[min].x) min = i;
	t = p[1];
	p[1] = p[min];
	p[min] = t;
	qsort(p, N);
	p[0] = p[N];
	for (M = 3, i = 4; i <= N; i++)
	{
		while (ccw(p[M], p[M-1], p[i]) >= 0) M--;
		M++;
		t = p[M];
		p[M] = p[i];
		p[i] = t;
	}
	return M;
}
/****** Convex Hull End *****************/