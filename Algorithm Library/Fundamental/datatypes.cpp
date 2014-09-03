#include <cstdio>

using namespace std;

struct LL
{
  int value;
  LL *next;
  LL *prev;
};

void addLL(LL *curr,int value)
{
	LL *new_node = new LL;
	new_node->value = value;
	curr->next = new_node;
	new_node->prev = curr;
}

void deleteLL(LL *st, int value)
{
	LL *t;

	if (st->value == value)
	{
		st->next->prev = NULL;
		st = st->next;
	}

	while (st->next != NULL) 
	{
		if (st->next->value == value)
		{
			t = st->next;

			st->next = st->next->next;
			if (st->next != NULL)
				st->next->prev = st;

			delete t;
			break;
		}
	}
}

void stackinit(LL *head)
{
	LL *z = new LL;
	head->value = 0;
	head->next = z;
	z->next = z;
}

void stack_push(LL *head, int value)
{
	LL *t = new LL;
	t->next = head->next;
	t->value = value;
	head->next = t;
}

int stack_pop(LL *head)
{
	LL *t;
	int key;

	t = head->next;
	head->next = t->next;

	key = t->value;

	delete t;

	return key;
}

void queueinit(LL *head, LL *tail)
{
	head->value = 0;
	tail->value = 0;
	head->next = tail;
	tail->prev = head; 
}

int queue_pop(LL *head)
{
    LL *t;
	int key;

	t = head->next;
	head->next = t->next;

	key = t->value;

	delete t;

	return key;	
}

void queue_push(LL *tail, int value)
{
	LL *t = new LL;
	t->value = value;
	t->next = tail;
	tail->prev->next = t;
	tail->prev = t;
}

int main()
{
	LL *head = new LL;
	LL *tail= new LL;
	queueinit(head, tail);
	queue_push(tail, 5);
	queue_push(tail, 6);
	queue_push(tail, 7);
	printf("%d",queue_pop(head));
	printf("%d",queue_pop(head));
	printf("%d",queue_pop(head));
}