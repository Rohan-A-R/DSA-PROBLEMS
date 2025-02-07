class Node:
    def __init__(self,val):
        self.val=val
        self.next=next

# to Delete The element From end
def remove_n_from_end(head,n):
        dummy = Node(0) 
        dummy.next = head
        left = dummy
        right = head 
    
        for _ in range(n):
            if right is None:  
                return head  
            right = right.next

        while right:
            left = left.next
            right = right.next

        if left.next:
            left.next = left.next.next

        return dummy.next 



# for  deleting from starting
def remove_n_from_start(head,n):
    if not head:
        return None
    if n==1:
        return head.next
    current=head
    count=1
    while current and count<n-1:
        current=current.next
        count+=1
    if not current or not current.next:
        return head
    current.next=current.next.next
    return head
    
         

          


    