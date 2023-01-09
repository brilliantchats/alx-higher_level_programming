#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: first elem of the list
 *
 * Return: 1 if its a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int *new_list;
	int length = 0, i, j = 0, last, palindrome = 1;
	listint_t *current = *head;

	if (*head == NULL)
		return (1);
	while (current != NULL)
	{
		length++;
		current = current->next;
	}
	current = *head;
	new_list = malloc(sizeof(int) * length);
	for (i = 0; i < length; i++)
	{
		new_list[i] = current->n;
		current = current->next;
	}
	last = length - 1;
	while (j < last)
	{
		if (new_list[j] != new_list[last])
		{
			palindrome = 0;
			break;
		}
		j++;
		last--;
	}
	free(new_list);
	return (palindrome);
}
