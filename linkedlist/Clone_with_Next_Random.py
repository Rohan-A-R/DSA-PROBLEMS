class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

# using hashMap
def clone_random_hash(head):
    node_map={}
    current=head
    while current:
        node_map[current]=Node(current.data) #this just cloning the nodes values
        current=current.next

    current=head
    while current:
        if current.next:
            node_map[current].next=node_map[current.next]
        if current.random:
            node_map[current].random=node_map[current.random]
        current=current.next

        return node_map[head]

# using space o(n)
def copyRandomList(head: Node) -> Node:
    if not head:
        return None

    # Step 1: Clone nodes and insert them after original nodes
    current = head
    while current:
        new_node = Node(current.val, current.next)
        current.next = new_node
        current = new_node.next

    # Step 2: Assign random pointers to the cloned nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Step 3: Separate the cloned list from the original
    original = head
    copy_head = head.next
    copy = copy_head

    while original:
        original.next = original.next.next
        copy.next = copy.next.next if copy.next else None
        original = original.next
        copy = copy.next

    return copy_head