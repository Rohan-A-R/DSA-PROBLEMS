class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node

    
    def print_link(self):
        current=self.head
        while current.next:
            print(current.data,end=' -> ')
            current=current.next

        print("None")


new_link=Linkedlist()
new_link.append(10)
new_link.append(11)
new_link.append(12)
new_link.append(13)
new_link.append(14)
new_link.print_link()


