class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def reverse_linkedlist1(head,left,right):
    if not head or left==right:
        return head
    dummy=Node(0)
    dummy.next=head
    prev=dummy

    for i in range(left-1):
        prev=prev.next



    current=prev.next
    prev_reverse=None
    for i  in range(left-right+1):
        temp=current.next
        current.next=prev_reverse
        prev_reverse=current
        current=temp

    prev.next.next=current
    prev.next=prev_reverse

    return dummy.next
