# Insert a Node at the Tail of a Linked List



def insertNodeAtTail(head, data):
    
    sys.setrecursionlimit(1000000) 
    if head == None:

        return SinglyLinkedListNode(data)
    else:
        if head.next == None:
            head.next = SinglyLinkedListNode(data)
        else:
            insertNodeAtTail(head.next,data)
    return  llist.head
