class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None


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
        new_node.prev=current

    def print_double(self):
        current=self.head
        while current:
            print(current.data,end=" <-> ")
            current=current.next
        print("None")

double_link=Linkedlist()
double_link.append(10)
double_link.append(11)
double_link.append(12)
double_link.append(13)
double_link.print_double()