# Get node value

def getNode(head, position):
    node = head
    list_len = 0
    
    while node != None:
        node = node.next
        list_len += 1
        
    node = head
    for _ in range(list_len - position - 1):
        node = node.next
    
    return node.data
