def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root):
    #set current to root of binary tree
    current=root
    stack=[]
    done=0
    while True:
        #reach the left most node of the current
        if current is not None:
            #place pointer o a tree node on the stack
            #before traversing the node's left subtree
            stack.append(current)
            current=current.left
            #backtrack from empty  subtree &visit node
            #at the top of the stack;however ,if the stack is empty u r done
        elif(stack):
            current=stack.pop()
            print(current.data,end=" ")
            current=current.right
        else:
            break
    print()
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
inorder(root)

        
