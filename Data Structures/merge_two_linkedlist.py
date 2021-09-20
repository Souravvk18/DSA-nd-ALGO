# Merged two sorted linked list


def mergeLists(headA, headB):
  if headA is None and headB is None:
    return None
  
  if headA is None:
    return headB

  if headB is None:
    return headA
  
  if headA.data < headB.data:
    smallerNode = headA
    smallerNode.next = mergeLists(headA.next, headB)
  else:
    smallerNode = headB
    smallerNode.next = mergeLists(headA, headB.next)
  
  return smallerNode