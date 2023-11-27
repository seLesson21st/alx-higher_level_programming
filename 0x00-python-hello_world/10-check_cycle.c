#include "lists.h"

/**
 * check_cycle - function that checks for loops in a linked list
 * @list: the head of linkrd list
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *quick, *slow;

	if (!list)
	{
		return (0);
	}
	slow = list;
	quick = list->next;
	while (quick && slow && quick->next)
	{
		if (slow == quick)
		{
			return (1);
		}
		slow = slow->next;
		quick = quick->next->next;
	}
	return (0);
}
