class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

# itrative method to find the middle value
def middle_linked(head):
    length=0
    current=head
    while current:
        length+=1
        current=current.next
    middle_index=length//2
    current=head
    for _ in range(middle_index):
        current=current.next
    return current.val

# itrative method to find the middle value and the countination of the list
def middle_linked(head):
    length=0
    current=head
    while current:
        length+=1
        current=current.next
    middle_index=length//2
    current=head
    for _ in range(middle_index):
        current=current.next
    return current

# easy and efficient method

def middleNode(head):
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow



