#create node
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.pre=n1
n1.next=n2
n3=Node(300)
n3.pre=n2
n2.next=n3
l.display()
def insert_start(self):
    n=Node(400)
    temp=self.head
    temp.prev=n
    n.next=temp
    self.head=n
def display(self):
    if self.head is None:
        print("empty")
    else:
        temp=self.head
        while temp:
            print(temp.data,"<-->",end=" ")
            temp=temp.next
def insert_end(self):
    n=Node(500)
    temp=self.head
    while temp.next is not None:
        temp=temp.next
    temp.next=n
    n.prev=temp
def display(self):
    if self.head is None:
        print("empty")
    else:
        temp=self.head
        while temp:
            print(temp.data,"<-->",end=" ")
            temp=temp.next
class dll:
    def __init__(self):
        self.head=None
    def insert_pos(self,pos):
        n=Node(44)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp #44's prev=200
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
    def display(self):
        if self.head is None:
            print("empty")
        else:
