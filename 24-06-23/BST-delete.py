'''logic
1.using "insert" create BST
2.input node to be deleted
3.spot or find the node which u want to delete(search)
4.once u find the node,check it comes under which category of delete
5.apply the delete concept
6.find inorder successor using separate function to replace with node to be deleted
'''
class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
#given a non-empty binary
#search tree,return the node
#with minm key value
#found in that tree,note that the entire tree doesn't need to be searched
def minValueNode(node):#right subtree
    current=node
    #loop down to find the leftmost leaf
    while(current.left is not None):
        current=current.left
    return current
#given a binary  search tree and a key,this function
#delete the key and returns the new root
def deleteNode(root,key):
    if root is None:
        return root
    #key<root,it lies in left subtree
    if key<root.key:
        root.left=deleteNode(root.left,key)
    elif(key>root.key):
        root.right=deleteNode(root.right,key)
        #if key is same as root's key ,then this is the
        #to be deleted
    else:
        #node with only one child or no child
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        #node with two children
        #get the successor inorder
        #smallest in the right subtree
        temp=minValueNode(root.right)
        #copy the inorder successor's
        #content  to this node
        root.key=temp.key
        #delete the inorder successor
        root.right=deleteNode(root.right,temp.key)
    return root
root=None
root=insert(root,50)
root=insert(root,30)
root=insert(root,20)
root=insert(root,40)
root=insert(root,70)
root=insert(root,60)
root=insert(root,80)
print("inorder")
inorder(root)
print("\n delete 20")
root=deleteNode(root,20)
print("inorder:modified tree")
inorder(root)
print("\n delete 30")
root=deleteNode(root,30)
print("inorder:modified tree")
inorder(root)
print("\n delete 50")
print("inorder:modified tree")
inorder(root)

