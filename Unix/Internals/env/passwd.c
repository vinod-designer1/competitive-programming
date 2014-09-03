#include <stdio.h>
#include <stdlib.h>
#include <pwd.h>

int main(int argc, char *argv[])
{
	struct passwd *pw;

	if (argc != 2)
		exit(-1);

	pw = getpwnam(argv[1]);
	if (pw != 0)
	{
		printf("Details for user %s\n", argv[1]);
		printf("  pw_passwd = %s\n", pw->pw_passwd);
		printf("  pw_uid    = %d\n", pw->pw_uid);
		printf("  pw_gid    = %d\n", pw->pw_gid);
		//printf("  pw_comment= %s\n", pw->pw_comment);
		printf("  pw_dir    = %s\n", pw->pw_dir);
		printf("  pw_shell  = %s\n", pw->pw_shell);
	}
	else
		printf("No match found for %s\n", argv[1]);
}