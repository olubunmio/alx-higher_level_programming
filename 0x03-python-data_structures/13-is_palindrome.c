#include "lists.h"

/**
 * rev_list - reverses a linked list
 * @head: pointer to the first node in the list
 * Return: returns nothing
 */
void rev_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the linked list
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/* find the middle of the linked list */
	/* for every one move 'slow' pointer goes, 'fast' makes two moves */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	dup = slow; /**
		     * at this point, (fast == NULL or fast->next == NULL)
		     * 'slow' is definately the at middle item (as in
		     * the case of an odd list) or the item just after it
		     * (in case of even list)
		     */

	/* reverse the items from the middle to the end */
	rev_list(&dup);

	/* compare from (1st item to middle) vs (last item to middle) */
	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
