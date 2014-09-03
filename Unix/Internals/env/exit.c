#include <stdio.h>
#include <stdlib.h>

void ex1()
{
	printf("ex1 called\n");
}

void ex2()
{
	printf("ex2 called\n");
}

int main()
{
	atexit(ex1);
	atexit(ex2);
	printf("About to call exit()\n");
	exit(0);
}