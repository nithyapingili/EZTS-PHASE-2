class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_beg(self):
        n=Node(300)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
    def insert_end(self):
        n=Node(50)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def insert_pos(self,pos):
        n=Node(44)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
    def display(self):
        if self.head is None:
            print("Empty!")
        else:
            temp=self.head
            while temp:
                if temp.next!=None:
                    print(temp.data,"<-->",end=" ")
                else:
                    print(temp.data,end=" ")
                temp=temp.next
obj=dll()
n1=Node(10)
obj.head=n1
n2=Node(11)
n1.next=n2
n2.prev=n1
n3=Node(20)
n2.next=n3
n3.prev=n2
n4=Node(45)
n3.next=n4
n4.prev=n3
obj.display()
print("\nAfter inserting at beginning")
obj.insert_beg()
obj.display()
print("\nAfter inserting at end")
obj.insert_end()
obj.display()
obj.insert_pos(2)
print("\n After inserting at 2nd pos")
obj.display()
