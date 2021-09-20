# delete duplicate value from sorted linked list

def removeDuplicates(head):
    node = head
    
    while node.next != None:
        if node.data == node.next.data:
            node.next = node.next.next
            continue
        node = node.next
  
    return head