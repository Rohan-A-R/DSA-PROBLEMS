class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

# Normal Method
def Merge_sorted_linked(head1,head2):
    dummy=Node(-1)
    current=dummy
    while head1 and head2:
        if head1.val < head2.val:
            current.next=head1
            head1=head1.next
        else:
            current.next=head2
            head2=head2.next
        current=current.next
    if head1:
        current.next=head1
    else:
        current.next=head2
    return dummy.next
    
# recurssive  Method

def merge_sorted_lists_recursive(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    if head1.val < head2.val:
        head1.next = merge_sorted_lists_recursive(head1.next, head2)
        return head1
    else:
        head2.next = merge_sorted_lists_recursive(head1, head2.next)
        return head2

