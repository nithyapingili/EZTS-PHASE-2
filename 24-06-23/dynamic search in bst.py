class Node:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def search(root, key):
    if root is None or root.data == key:
        return root
    if root.data < key:
        return search(root.right, key)
    return search(root.left, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)


#create
def createBST(nums):
    root = None
    for num in nums:
        root = insert(root, num)
    return root

#given list
nums = list(map(int,input().split()))

#create the binary search tree
bst = createBST(nums)

#perform search operation
search_key = int(input("Enter:"))
result = search(bst, search_key)
if result is not None:
    print(f"Element {search_key} found in the BST")
else:
    print(f"Element {search_key} not found in the BST")

#inorder
print("INORDER:")
inorder(bst)
