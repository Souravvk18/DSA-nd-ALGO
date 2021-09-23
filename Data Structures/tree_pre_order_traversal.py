def preOrder(root):
    if root:
        print(root.info, end=' ') #print on same line
        preOrder(root.left)
        preOrder(root.right)