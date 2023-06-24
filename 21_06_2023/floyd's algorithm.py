class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        #insert a newnode at the beginning
        def push(self,new_data):
            new_node=Node(new_data)
            new_node.next=self.head
            self.head=new_node
        def detectandremoveloop(self):
            if self.head is None:#LL empty
                return
            if self.head.next is None:#LL has one node
                return
            slow=self.head
            fast=self.head
            while(slow and fast and fast.next):
                slow=slow.next
                fast=fast.next.next
                #if slow and fast meet at some point
                #there is a loop
                if slow==fast:
                    print("meeting point",slow.data)
                    slow=self.head
                    #finding the beginning of the loop
                    while(slow.next!=fast.next):
                        slow=slow.next
                        fast=fast.next
                        #sinc fast.next is the looping point
                    print("start of loop",fast.next.data)
                    fast.next=None #remove loop
            def printlist(self):
                temp=self.head
                while(temp):
                    print(temp.data,end=' ')
                    temp=temp.next
llist=LinkedList()
llist.head=Node(50)
llist.head.next=Node(20)
llist.head.next.next=Node(15)
llist.head.next.next.next=Node(4)
llist.head.next.next.next.next=Node(10)
#create a loop for testing
extra=Node(1)
llist.head.next.next.next.next.next=extra
extra.next=llist.head.next
#llist.printlist()
llist.detectandremoveloop()
print("Linked list after removing loop")
llist.printList()




                    
                
        
