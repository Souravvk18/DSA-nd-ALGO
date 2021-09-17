# Insert a node at a specific position in a linked list

# solution
def insertNodeAtPosition(head, data, position):
        # Null case
        if head is None:
                return SinglyLinkedListNode(data)

        cur = head

        for _ in range(position - 1):
                cur = cur.next

        cur.next, cur.next.next = SinglyLinkedListNode(data), cur.next

        return head
