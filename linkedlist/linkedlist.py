# Basic Structure of a Node

class Node:
    def __init__(self,data):
        self.data =data
        self.next=None

# 1. Insertion 

def insert_at_begining(head,data):
    new_node=Node(data)
    new_node.next=head
    return new_node

# Deletion

def deletion_from_beginning(head):
    if not head:
        return None
    return head.next

# traversal
def traversal(head):
    current=head
    while current:
        print(current.data,end='->')
        current=current.next
    print("none")

# search

def search(head,key):
    current=head
    while current:
        if current.data==key:
            return True
        current=current.next
    return False

# Creating and Displaying a Singly Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Singly_Linkedlist:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node

    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("none")

ll=Singly_Linkedlist()
ll.append(10)
ll.append(11)
ll.append(12)
ll.append(13)
ll.display()




        

