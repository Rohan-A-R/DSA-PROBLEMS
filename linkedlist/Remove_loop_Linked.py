class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

# detect the loop       
def  Remove_loop_Linked_List(head):
    slow,fast=head,head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            break
    else:   #if statement is breaked so we can't use else  statement rember that
        return True
        
# find the starting of the cycle
    slow=head
    while slow!=fast:
        slow=slow.next
        fast=fast.next

# find the Last node 
    while fast.next!=slow:
        fast=fast.next
    fast.next=None
    return  True
        
# Usinh hashSet
def remove_loop_using_set(head):
    visted=set()
    curreent=head
    prev=None
    while curreent:
        if curreent in visted:
            prev.next=None
            return True
        visted.add(curreent)
        prev=curreent
        curreent=curreent.next
    return True #if no node is present