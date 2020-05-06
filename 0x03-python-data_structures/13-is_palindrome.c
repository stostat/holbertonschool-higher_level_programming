#include "lists.h"
/**
* is_palindrome - checks for palindromes 
* @head: pointer to the head
*Return: 1 if true 0 if false
*/

int is_palindrome(listint_t **head)
{
	listint_t *hd = *head;
	int i = 0, j = 0;
	int *nval;

	if (!hd || !hd->next)
		return (1);

	while (hd)
	{
		nval[i] = hd->n;
		hd = hd->next;
		i++;
	}

	i -= 1;

	while (j <= i / 2)
	{
		if (nval[j] != nval[i - j])
			return (0);
		j++;
	}
	return (1);
}