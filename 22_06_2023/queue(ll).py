class Node:
    def __int__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        self.last=None
    def enqueue(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next=Node(data)
            self.last=self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return=self.head.data
            self.head=self.head.next
            return to_return
a_queue=Queue()
while True:
    print('enqueue <value>')
    print('dequeue')
    print('quit')
    #by using split,do will become a list,split
    #works with string
    do=input('what would you like to do').split()
    print("do[0]:",do[0])n
    operation=do[0].strip().lower()
    if operation=='enqueue':
        a_queue.enq(int(do[l])
    elif operation=='dequeue':
        dequeue=a_queue.dq()
        if dequeued is None:
            print("queue is empty")
        else:
            print("dequeued value:",int(dequeued))
    elif op=='quit':
        break
    
