from Helper_function import  ListNode, create_linked_list, print_linked_list

def reorder_list(head):
    if not head or not head.next or not head.next.next:
        return head
# first we need find the middle element  
    slow,fast=head,head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

# now reverse the second half
    prev,currrent=None,slow.next
    slow.next=None
    while currrent:
        temp=currrent.next
        currrent.next=prev
        prev=currrent
        currrent=temp

#  now mwerge to parts
    first,second=head,prev
    while second:
        temp1=first.next
        temp2=second.next
        first.next=second
        second.next=temp1
        first=temp1
        second=temp2
    return head

values=[1,7,3,4]
head=create_linked_list(values)
reoder=reorder_list(head)
print_linked_list(reoder)


# using Stack and Extra place
def reorder_using_stack(head):
    if not head or not head.next:
        return head

    # Step 1: Push all nodes into a stack
    stack = []
    temp = head
    while temp:
        stack.append(temp)
        temp = temp.next

    # Step 2: Find middle of the linked list
    n = len(stack)
    mid = n // 2  # Middle index

    # Step 3: Reorder using the stack
    temp = head
    for _ in range(mid):
        last_node = stack.pop()
        last_node.next = temp.next
        temp.next = last_node
        temp = last_node.next  # Move to the next original node

    # Step 4: Set the next of the last node to None
    temp.next = None

    return head







