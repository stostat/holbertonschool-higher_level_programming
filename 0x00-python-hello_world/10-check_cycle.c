#include "lists.h"
/**
 * check_cycle - finds loops in a linked list
 * @list: pointerto the head of the list
 * Return: 1 on loop 0 whrn no loop found
 */

int check_cycle(listint_t *list)
{
	listint_t *turtle = NULL;
	listint_t *hare = NULL;

	turtle = list;
	hare = list;

	while (list && hare && hare->next && hare->next->next)
	{
		turtle = turtle->next;
		hare = hare->next->next;
		if (turtle == hare)
		return (1);
	}
	return (0);
}
