#include "lists.h"

/**
 *check_cycle - checks for loops in linked lists
 *@list: pointer to linked lists
 *Return: returns 0 for no cycles or loops and 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_p = list, *fast_p = list;

	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
		if (slow_p == fast_p)
		{
			return (1);
		}
	}
	return (0);
}
