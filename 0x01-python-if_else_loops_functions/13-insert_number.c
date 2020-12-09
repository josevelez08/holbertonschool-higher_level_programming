#include "lists.h"
/**
 * insert_node - insert a node
 * @head: the head of the list
 * @number: compare
 * Return: the new list
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp1, *tmp2, *new;

	new = malloc(sizeof(listint_t *));
	if (new == NULL)
	{ return (NULL); }
	tmp1 = *head;
	tmp2 = *head;

	new->n = number;
	new->next = NULL;
	if ((*head)->n >= number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
	tmp1 = tmp1->next;

	while (tmp1 != NULL)
	{
		if (tmp1->n >= number)
		{
			tmp2->next = new;
			new->next = tmp1;
			break;
		}
		else
		{
			tmp1 = tmp1->next;
			tmp2 = tmp2->next;
		}
	}
	if (tmp1 == NULL)
	{
		tmp2->next = new;
		new->next = tmp1;
	}
	}
	return (new);
}
