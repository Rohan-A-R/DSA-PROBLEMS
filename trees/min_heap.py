class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def push(self, value):
        """Insert a value into the heap and maintain heap property."""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        """Move the inserted element up to maintain the heap property."""
        parent = self._parent(index)
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = self._parent(index)

    def pop(self):
        """Remove and return the smallest element (root of min-heap)."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root_value = self.heap[0]
        self.heap[0] = self.heap.pop()  # Replace root with last element
        self._heapify_down(0)
        return root_value

    def _heapify_down(self, index):
        """Move the root element down to maintain the heap property."""
        smallest = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def peek(self):
        """Return the smallest element without removing it."""
        return self.heap[0] if self.heap else None

    def display(self):
        """Print the heap as an array."""
        print(self.heap)

# Example Usage
heap = MinHeap()
heap.push(10)
heap.push(5)
heap.push(20)
heap.push(2)
heap.push(15)

heap.display()  # Output: [2, 5, 20, 10, 15]
print(heap.pop())  # Output: 2 (smallest element)
heap.display()  # Output: [5, 10, 20, 15]
