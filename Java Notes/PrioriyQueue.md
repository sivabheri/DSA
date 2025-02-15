# PriorityQueue in Java

## Overview

- `PriorityQueue` is a part of `java.util` package.
- It is an implementation of the **Queue** interface that maintains elements in a **natural order** (min-heap by default).
- Elements are **ordered based on priority** rather than insertion order.
- It **does not allow null elements**.

## Import Statement

```java
import java.util.PriorityQueue;
```

## Initialization

```java
PriorityQueue<Type> pq = new PriorityQueue<>(); // Default min-heap
```

Or with a custom comparator (for max-heap):

```java
PriorityQueue<Type> pq = new PriorityQueue<>(Comparator.reverseOrder());
```

## Operations

### 1. Adding Elements

```java
pq.add(element);
pq.offer(element); // Similar to add, but returns false if the queue is full
```

### 2. Accessing the Highest Priority Element

```java
Type topElement = pq.peek(); // Retrieves but does not remove
```

### 3. Removing Elements

```java
pq.poll(); // Retrieves and removes the highest priority element
pq.remove(element); // Removes a specific element
```

### 4. Checking If an Element Exists

```java
boolean exists = pq.contains(element);
```

### 5. Getting Queue Size

```java
int size = pq.size();
```

### 6. Iterating Over PriorityQueue

```java
for (Type x : pq) {
    System.out.println(x);
}
```

### 7. Clearing the PriorityQueue

```java
pq.clear();
```

## Example Program

```java
import java.util.PriorityQueue;
import java.util.Comparator;

public class PriorityQueueExample {
    public static void main(String[] args) {
        // Min-Heap PriorityQueue (default)
        PriorityQueue<Integer> pq = new PriorityQueue<>();
      
        // Adding elements
        pq.add(10);
        pq.add(5);
        pq.add(20);
        pq.add(15);
      
        // Accessing and removing elements
        System.out.println("Top element: " + pq.peek());
      
        while (!pq.isEmpty()) {
            System.out.println("Removed: " + pq.poll());
        }
      
        // Max-Heap PriorityQueue
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        maxHeap.add(10);
        maxHeap.add(5);
        maxHeap.add(20);
        maxHeap.add(15);
      
        System.out.println("Max-Heap Order:");
        while (!maxHeap.isEmpty()) {
            System.out.println(maxHeap.poll());
        }
    }
}
```

## When to Use PriorityQueue?

- When you need to process elements **by priority** rather than insertion order.
- When **sorting dynamically** as elements are inserted is required.
- When implementing **Dijkstra’s algorithm, Huffman coding, or event-driven simulations**.
