#delete a node from a linked list

def deleteNode(llist, position):
    # Write your code here
    if position == 0:
        llist = llist.next
    else:
        node = llist
        for _ in range(position-1):
            node = node.next
        
        node.next = node.next.next
        
    return llist