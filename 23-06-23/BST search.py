class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
def search(root,key):
    #base cases:root is null or key is present
    if root is None or root.val==key:
        return root
    #key is greater than root's key
    if root.val<key:
        return search(root.right.key)
    #key is smallr than root's key
    return search(root.left,key)
#inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
r=Node(50)
r=insert(r,30)
r=insert(r,20)
r=insert(r,40)
r=insert(r,70)
r=insert(r,60)
r=insert(r,80)
inorder(r)


