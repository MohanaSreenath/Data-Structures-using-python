class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        ptr=self.head
        while ptr.next:
            ptr=ptr.next
        ptr.next=new_node
    
    def display(self):
        current=self.head
        while current:
            print(current.data,"->",end=" ")
            current=current.next
        print("\n Linkedlist is empty is munda")

mylinkedlist = Linkedlist()
mylinkedlist.display()
for i in range(0,10):
    mylinkedlist.append(i)
mylinkedlist.display()
