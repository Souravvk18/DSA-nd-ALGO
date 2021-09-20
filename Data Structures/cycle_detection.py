# Detect a cycle in a linked list

def has_cycle(head):
    cnt = 0
    node = head
    
    if head is None:
        return 0
    
    while node != None:
        node = node.next
        cnt += 1
        if cnt > 100:
            return 1
    
    return 0