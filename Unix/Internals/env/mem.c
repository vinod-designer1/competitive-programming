
// allted memory while process creation
// initialized in data section of bin file on disk
char *error_message = "Access rights not granted";

// storage required not store in bin file
// but allocated as part of process in BSS
// within data segement during process creation and is zero filled.
char message[26];

int main(int argc, char *argv[])
{
	// this local variables in functions
	// are pushed on to stack 
	// de-allocated on return from the function
	// any function
	int a;
	char* pw;
	// for static variable space is allocated in data segment
	// stackoverflow occurs where the stack frows down over 
	// amount of memory allocated
	static in x = 4;
}