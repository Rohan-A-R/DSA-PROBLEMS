class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# using stack

def Linked_List_Group_Reverse(head,k):
    if not head or k == 1:
        return head
    
    # Dummy node to handle edge cases like when head is None
    dummy = Node(0)
    dummy.next = head
    prev_group_end = dummy

    # Stack to reverse k nodes
    stack = []
    current = head
    
    while current:
        stack.append(current)
        if len(stack) == k:
            # Reverse the group
            while stack:
                prev_group_end.next = stack.pop()
                prev_group_end = prev_group_end.next
            # Link the last node in the reversed group to the next node
            prev_group_end.next = current
            stack = []
        current = current.next
    
    # If there are remaining nodes that are fewer than k, do not reverse them
    return dummy.next


# Easy method

def Linked_List_Group_Reverse_easy(head,k):
    if not  head or k<=1:
        return head
    
    count=0
    temp=head
    while temp:
        count+=1
        temp=temp.next
    
    dummy=Node(0)   #we create a dummy node
    dummy.next=head  #we assign dummy node to head
    prev_end=dummy   #we assign dummy  to prev because to track the end of the linkedlist
   
    while count>=k:
        prev=None
        current=prev_end.next
        next_group=current
        for _ in range(k):
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        
        prev_end.next.next=current
        temp=prev_end.next
        prev_end.next=prev
        prev_end=temp
        count-=k
    
    return dummy.next

# 1 -> 2 -> 3 -> 4 -> 5 -> 6, k = 3
# prev_end.next.next = current → 1.next = 4
# temp = prev_end.next → temp = 1
# prev_end.next = prev → dummy.next = 3
# prev_end = temp → prev_end = 1
# count -= k → count = 3
# Final Linked List After First Group


        


    
    

