from Helper_function import  ListNode, create_linked_list, print_linked_list

def palindrome_linkeddlist(head):
    if not head or not head.next:
        return True 
    slow,fast=head,head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

    prev,currrent=None,slow
    while currrent:
        prev_node=currrent.next
        currrent.next=prev
        prev=currrent
        currrent=prev_node

    first,second=head,prev
    while second:
        if first.val!=second.val:
            return False
        first=first.next
        second=second.next
    return True

values=[1, 1 ,2 ,1 ,2, 1]
head=create_linked_list(values)
result=palindrome_linkeddlist(head)
print(result)
# print_linked_list(result)
