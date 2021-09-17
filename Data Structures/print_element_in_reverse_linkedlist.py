#print the element of a linked list in reverse 

def reversePrint(head):
    if head is None:
        return
    else:
        out = []
        node = head
        
        while node != None:
            out.append(node.data)
            node = node.next
            
        print("\n".join(map(str, out[::-1])))