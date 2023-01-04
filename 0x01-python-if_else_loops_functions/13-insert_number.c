#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * empty_list - Handles an empty list
 * @node: the new node to be added
 * @num: the integer
 *
 * Return: the address of the new node
 */
listint_t *empty_list(listint_t *node, int num)
{
	node->n = num;
	node->next = NULL;
	return (node);
}
/**
 * insert_node - Inserts a node into a sorted list
 * @head: the head of the linked list
 * @number: the integer value of the new node to be inserted
 *
 * Return: address of the new node, NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *previous = *head, *new;
	int inserted = 0;

	new = malloc(sizeof(listint_t));
	if (*head == NULL)
		return (empty_list(new, number));
	if (new == NULL)
		return (NULL);
	new->n = number;
	while (current != NULL)
	{
		if (current->n > new->n)
		{
			if (current == previous)
			{
				new->next = current;
				*head = new;
				inserted = 1;
			}
			else
			{
				new->next = current;
				previous->next = new;
				inserted = 1;
			}
			break;
		}
		previous = current;
		current = current->next;
	}
	if (inserted == 0)
	{
		new->next = NULL;
		previous->next = new;
	}
	return (new);
}
