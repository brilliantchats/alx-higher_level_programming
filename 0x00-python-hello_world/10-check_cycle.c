#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - Checks a linked list for any cycles
 * @list: the list to be checked
 *
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *node = list;
	listint_t *tmp;
	int found = 0, len = 0, j;

	while (node != NULL)
	{
		if (node->next == NULL)
			break;
		for (tmp = list, j = 0; j < (len + 1); tmp = tmp->next, j++)
		{
			if (tmp == node->next)
			{
				found = 1;
				break;
			}
		}
		if (found)
			break;
		node = node->next;
		len++;
	}
	if (found)
		return (1);
	return (0);
}
