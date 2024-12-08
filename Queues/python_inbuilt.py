from queue import Queue

# Create a Queue
q = Queue()

# Enqueue items
q.put(1)
q.put(2)
q.put(3)

# Check the size of the queue
print("Queue size:", q.qsize())  # Output: Queue size: 3

# Peek at the front item (not directly available, so we use a workaround)
if not q.empty():
    front_item = q.queue[0]  # Accessing the underlying deque directly
    print("Front item:", front_item)  # Output: Front item: 1

# Dequeue items
print("Dequeued item:", q.get())  # Output: Dequeued item: 1
print("Dequeued item:", q.get())  # Output: Dequeued item: 2

# Check the size of the queue after dequeuing
print("Queue size after dequeue:", q.qsize())  # Output: Queue size after dequeue: 1

# Dequeue the last item
print("Dequeued item:", q.get())  # Output: Dequeued item: 3

# Check if the queue is empty
print("Is the queue empty?", q.empty())  # Output: Is the queue empty? True