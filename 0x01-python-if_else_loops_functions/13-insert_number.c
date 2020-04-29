#include "lists.h"
/**
 * listint_t - adds node between minor and bigger number
 * @head: pointer to head of linked list
 * @number: number inserted in node
 * Return: node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head;
	listint_t *new = NULL;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (tmp->n >= number || !tmp)
	{
		new->next = tmp;
		*head = new;
		return (new);
	}
	while (tmp && tmp->next->n < number)
		tmp = tmp->next;
	new->next = tmp->next;
	tmp->next = new;
	return (new);
}
