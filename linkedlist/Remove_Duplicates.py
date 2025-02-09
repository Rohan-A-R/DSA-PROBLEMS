class Node:
    def __init__(self,head):
        self.next=head
        self.next=None
    
    def Remove_Duplicates_linked_list(head):
        current=head
        while  current and current.next:
            if current.val==current.next.val:
                current.next=current.next.next
            else:
                current=current.next
            
            return head

# using hash set
    def Remove_Duplicates_linked_list_set(head):
        current=head
        visted=set()
        while  current and current.next:
            if current.val in visted:
                current.next=current.next.next
            else:
                visted.add(current.val)
                current=current.next
            
            return head

# for unsorted linkedlist
    def Remove_Duplicates_linked_list_unsorted(head):
            if not head or not head.next:
                return head

            hash_set = set()
            curr = head
            prev = None

            while curr is not None:
                if curr.data in hash_set:
                    prev.next = curr.next
                    curr = curr.next
                else:
                    hash_set.add(curr.data)
                    prev = curr
                    curr = curr.next

            return head
        