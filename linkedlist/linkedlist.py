# Basic Structure of a Node
class node:
    def __init__(self,data):
        self.data=data
        self.next=None      

# 1. Insertion

def insert_at_beginning(head,data):
    new_node=node(data)
    new_node.next=head
    return new_node

#2. Deletion

def delete_from_beginning(head):
    if not head:
        return None
    return head.next


# 3. Traversal

def traverse(head):
    current=head
    while current:
        print(current.data,end="->")
        current =current.next
    print("none")


# 4. Search

def Search(head,key):
    current=head
    while current:
        if current.data==key:
            return True
        current = current.next
    return False


# Examples
# Creating and Displaying a Singly Linked List

class Node:
     def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None


    def append(self,data): 
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            current =self.head
            while current.next:
                current = current.next
            current.next=new_node
    
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=  current.next
        print("None")

new=SinglyLinkedList()
new.append(1)
new.append(2)
new.append(3)
new.append(4)
new.display()

        



