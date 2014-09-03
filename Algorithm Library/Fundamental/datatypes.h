#ifndef __DATA_TYPES__
#define __DATA_TYPES__

struct LL
{
	int value;
	LL *next;
	LL *prev;
};

void addLL(int);
void deleteLL(int);

#endif //__DATA_TYPES__