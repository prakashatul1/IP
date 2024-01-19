class MaxQueue:
    def __init__(self):
        self.queue = []  # Main queue for enqueue and dequeue operations
        self.maxElements = []  # To keep track of max elements

    def enqueue(self, value):
        """Add an element to the end of the queue."""
        self.queue.append(value)

        # Remove elements from maxElements if they are less than the new element
        while self.maxElements and self.maxElements[-1] < value:
            self.maxElements.pop()

        # Add the new element to maxElements
        self.maxElements.append(value)

    def dequeue(self):
        """Remove an element from the front of the queue."""
        if not self.queue:
            raise IndexError("dequeue from an empty queue")

        # If the element leaving the queue is the current max, remove it from maxElements
        if self.queue[0] == self.maxElements[0]:
            self.maxElements.pop(0)  # This operation is O(1) because it's always the first element

        return self.queue.pop(0)

    def getMax(self):
        """Get the maximum element in the queue."""
        if not self.maxElements:
            raise IndexError("getMax from an empty queue")

        return self.maxElements[0]


# Example usage
q = MaxQueue()
q.enqueue(3)
q.enqueue(1)
q.enqueue(5)
print("Max:", q.getMax())  # Should return 5
q.dequeue()
print("Max after one dequeue:", q.getMax())  # Should return 5
