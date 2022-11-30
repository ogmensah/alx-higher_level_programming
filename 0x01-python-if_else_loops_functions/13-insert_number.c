#include "lists.h"

/**
 * insert_nod - inserts new node in a linked list
 * @head: linked list pointer
 * @ number: value held by new node to the new node
 *
 * Return: returns pointer to the new node inserted
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *prev_node, *next_node;

	if (*head == NULL)
	{
		return NULL;
	}

	new_node = (listint_t *)malloc(sizeof(listint_t));

	prev_node = *head;
	new_node->n = number;

	if (prev_node->n > number)
	{
		new_node->next = prev_node;
		*head = new_node;
		return (new_node);
	}

	while (next_node->next != NULL && next_node->n <= number)
	{
		next_node = prev_node->next;
	}
	new_node->next = next_node;
	prev_node->next = new_node;
	return (new_node);
}
