class Node:
    def __init__(self,val):
        self.val=val
        self.next=next

def Kth_End_Linked_List(head,k):
    slow,fast=head,head
    for _ in range(k):
        if not fast:
            return -1
        fast=fast.next

    while fast:
        slow=slow.next
        fast=fast.next
    return slow.val
    
