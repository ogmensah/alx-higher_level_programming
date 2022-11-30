#include "lists.h"

/**
 * insert_node - inserts new node in a linked list
 * @head: linked list pointer
 * @number: value held by new node to the new node
 *
 * Return: returns pointer to the new node inserted
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *prev_node, *next_node;

	new_node = (listint_t *)malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}

	prev_node = *head;
	new_node->n = number;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	if (prev_node->next == NULL)
	{
		prev_node->next = new_node;
		return (new_node);
	}
	if (prev_node->n > number)
	{
		new_node->next = prev_node;
		*head = new_node;
		return (new_node);
	}

	next_node = prev_node->next;
	while (next_node->next != NULL)
	{
		if (next_node->n > number)
		{
			new_node->next = next_node;
        		prev_node->next = new_node;
        		return (new_node);
		}
		prev_node = next_node;
		next_node = next_node->next;
	}
	next_node->next = new_node;
	return (new_node);
}
