class link:
    def __init__(self,data):
        self.data=data
        self.next=None

    def mid_element(head):
        current=head
        count=0
        while current:
            current=current.next
            count+=1

        mid=count//2
        for _ in range(mid):
            current=current.next
        current.next=current.next.next
        return head

    

        