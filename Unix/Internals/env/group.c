#include <stdio.h>
#include <stdlib.h>
#include <grp.h>

int main(int argc, char *argv[])
{
	struct group *grp;

	if (argc != 2)
		exit(-1);

	grp = getgrgid(atoi(argv[1]));
	printf("group name = %s\n", grp->gr_name);
}