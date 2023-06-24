class node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__ (self):
        self.head=None
    def insert_position(self,pos,data):
        np=node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
    def display(self):
       if self.head==None:
           print("Linked List is empty!")
       else:
           temp=self.head
           while temp:
                if temp.next!=None:
                    print(temp.data,"->",end="")
                else:
                    print(temp.data,end="")
                temp=temp.next
obj=singlelinkedlist()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
print("Before inserting at a position:")
obj.display()
obj.insert_position(3,100)
print("\nAfter inserting at a position:")
obj.display()
