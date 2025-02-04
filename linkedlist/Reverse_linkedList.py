# Reverse a singly linked list.
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

    def reverse_linkedlist(self,head):
        prev=None
        current=head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        return prev

#  count the number of nodes in the reversed linked list.
def reverse_and_count(head):
    prev=None
    current=head
    count=0
    while current:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node
        count+=1
    return prev,count

        