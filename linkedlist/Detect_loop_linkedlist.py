class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

# Hashing Method Using HashSet

def cycle_set(head):
    current=head
    visited=set()
    while current:
        if current in visited:
            return True
        visited.add(current)
        current=current.next
    return False


# Hashing Method Using HashMap

def cycle_hash(head):
    current=head
    visited={}
    while current:
        if current in visited:
            return True
        visited[current]=True
        current=current.next
    return False



        