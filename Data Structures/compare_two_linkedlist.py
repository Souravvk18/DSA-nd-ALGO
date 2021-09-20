# Compare two linked lists


def compare_lists(llist1, llist2):
    if llist1 is None and llist2 is None:
        return 0
    else:
        nodeA = llist1
        nodeB = llist2
        while nodeA and nodeB:
            if nodeA.data != nodeB.data:
                return 0
            nodeA = nodeA.next
            nodeB = nodeB.next
        
        if nodeA is None and nodeB is None:
            return 1
        else:
            return 0