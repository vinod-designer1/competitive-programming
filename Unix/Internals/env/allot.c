#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> 

//sbrk and brk used for malloc, free, realloc
int main()
{
	char *obrk;
	char *nbrk;

	obrk = sbrk(0);
	printf("current break address = 0x%x\n", obrk);
	// allocate 32 bytes
	nbrk = sbrk(32);
	printf("new break address     = 0x%x\n", nbrk);
	printf("    difference        = %ld bytes\n", nbrk-obrk);
}