# Print the Elements of a Linked List

def printLinkedList(head):
    node = head
    while node != None:
        print(node.data)
        node = node.next
