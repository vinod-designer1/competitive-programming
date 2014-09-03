#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


extern char **environ; // this also act stores environment variables

int main(int argc, char *argv[], char *envp[]) 
// argc = no of arguments
// argv = array of arguments
// envp = shell environment variables passed to program
{
	int x;
	char buf[32];

	if (argc != 2)
		exit(-1);

	printf("The value of ARG_MAX = %ld\n", sysconf(_SC_ARG_MAX));
	printf("Current value for PS1 = %s\n", getenv("PS1"));
	sprintf(buf, "PS1=%s", argv[1]);
	putenv(buf);
	printf("new value for PS1 = \"%s\"\n", getenv("PS1"));

	printf("argc = %d\n", argc);
	for (x = 0; x < argc; ++x)
	{
		printf("argv[%d] = %s\n", x, argv[x]);
	}

	for (x = 0; x < 10; ++x)
	{
		if (environ[x] != NULL)
			printf("environ[%x] = %s\n", x, environ[x]);
	}
}