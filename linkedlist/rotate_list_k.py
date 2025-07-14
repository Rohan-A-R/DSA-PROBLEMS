class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    
    def rotate(head,k):
        if not head or not  head.next or k==0:
            return head
        tail=head
        count=1
        while tail.next:
            tail=tail.next
            count+=1

        k=k%count
        if k==0:
            return head
        
        current=head
        for _ in range(count-k-1):
            current=current.next

        new_head=current.next
        current.next=None
        tail.next=head
        return new_head


        