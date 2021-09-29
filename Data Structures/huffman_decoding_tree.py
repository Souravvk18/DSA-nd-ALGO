def is_leaf(root):
    if root.right == None and root.left == None:
        return True
    else:
        return False

def decodeHuff(root, s):
    #Enter Your Code Here
    node = root
    output = ''
    for dig in s:
        #print "dig = {} node.freq = {}".format(dig, node.freq)
        if dig == '0':
            if is_leaf(node.left):
                output += node.left.data
                node = root
            else:
                node = node.left
        else:
            if is_leaf(node.right):
                output += node.right.data
                node = root
            else:
                node = node.right
    
    print (output)