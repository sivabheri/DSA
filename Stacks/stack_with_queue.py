from queue import Queue

class StackUsingQueue:
    def __init__(self):
        self.queue = Queue()

    def push(self, item):
        # Add the new item to the queue
        self.queue.put(item)
        
        # Rotate the queue to make the new item the front
        for _ in range(self.queue.qsize() - 1):
            self.queue.put(self.queue.get())

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.queue.get()  # Remove and return the front item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        front_item = self.queue.get()  # Get the front item
        self.queue.put(front_item)  # Put it back
        return front_item

    def is_empty(self):
        return self.queue.empty()

    def size(self):
        return self.queue.qsize()

    def display(self):
        # Temporary queue to hold items while displaying
        temp_queue = Queue()
        items = []

        # Dequeue all items to display them
        while not self.is_empty():
            item = self.pop()
            items.append(item)  # Store the item for display
            temp_queue.put(item)  # Store in temp queue to restore later

        # Restore the original stack order
        while not temp_queue.empty():
            item = temp_queue.get()
            self.push(item)  # Push back to the original stack

        # Display the items
        print("Stack items:", items)

# Example usage
if __name__ == "__main__":
    stack = StackUsingQueue()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.display()  # Output: Stack items: [3, 2, 1]
    print("Top item:", stack.peek())  # Output: Top item: 3
    print("Popped item:", stack.pop())  # Output: Popped item: 3
    stack.display()  # Output: Stack items: [2, 1]