class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
# Separate Lists  using dummy Node
def rearrange_linked_list(head):
    if not head or not head.next:
        return head

    even_node=Node(0)
    odd_node=Node(0)
    
    even=even_node
    odd=odd_node

    currrent=head
    count=1
    while currrent:
        if count%2==1:
            odd.next=currrent
            odd=odd.next
        else:
            even.next=currrent
            even=even.next
        currrent=currrent.next
        count+=1

    odd.next=even_node.next
    even.next=None
    return odd_node.next
    
# easy method anf effecient method

def rearrange_linked_list_method2(head):
    odd=head
    even=head.next
    even_head=even
    while even and even.next:
        odd.next=even.next
        odd=odd.next

        even.next=odd.next
        even=even.next

    odd.next=even_head

    return head
