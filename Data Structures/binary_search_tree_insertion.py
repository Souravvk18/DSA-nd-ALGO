class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 


# write your code here.

def insert(self, val):
        cur = self.root
        if not cur: 
            self.root = Node(val)
            return self.root
        
        while cur:
            if cur.info > val: 
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(val)
                    break
            else: 
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(val)
                    break
        
        return self.root