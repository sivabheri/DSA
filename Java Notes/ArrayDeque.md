# ArrayDeque in Java

## Overview

- `ArrayDeque` is a part of `java.util` package.
- Implements `Deque` (Double-Ended Queue) and allows insertion and deletion from both ends.
- **Faster than Stack and LinkedList** for stack and queue operations.
- **No capacity restrictions**, dynamically grows as needed.
- **Does not allow null elements**.

## Import Statement

```java
import java.util.ArrayDeque;
```

## Initialization

```java
ArrayDeque<Type> arrayDeque = new ArrayDeque<>();
```

## Operations

### 1. Adding Elements

```java
arrayDeque.addFirst(element); // Adds at the front
arrayDeque.addLast(element);  // Adds at the end
arrayDeque.offerFirst(element); // Adds at the front, returns false if full
arrayDeque.offerLast(element);  // Adds at the end, returns false if full
```

### 2. Accessing Elements

```java
Type first = arrayDeque.getFirst(); // Retrieves first element
Type last = arrayDeque.getLast();   // Retrieves last element
```

### 3. Removing Elements

```java
arrayDeque.removeFirst(); // Removes first element
arrayDeque.removeLast();  // Removes last element
arrayDeque.pollFirst();   // Removes first element, returns null if empty
arrayDeque.pollLast();    // Removes last element, returns null if empty
```

### 4. Checking If an Element Exists

```java
boolean exists = arrayDeque.contains(element);
```

### 5. Getting Size

```java
int size = arrayDeque.size();
```

### 6. Iterating Over ArrayDeque

```java
for (Type x : arrayDeque) {
    System.out.println(x);
}
```

### 7. Clearing the ArrayDeque

```java
arrayDeque.clear();
```

## Example Program

```java
import java.util.ArrayDeque;

public class ArrayDequeExample {
    public static void main(String[] args) {
        ArrayDeque<Integer> arrayDeque = new ArrayDeque<>();
      
        // Adding elements
        arrayDeque.addFirst(10);
        arrayDeque.addLast(20);
        arrayDeque.addFirst(5);
      
        // Accessing elements
        System.out.println("First: " + arrayDeque.getFirst());
        System.out.println("Last: " + arrayDeque.getLast());
      
        // Removing elements
        arrayDeque.removeFirst();
        arrayDeque.removeLast();
      
        // Iterating over ArrayDeque
        for (Integer num : arrayDeque) {
            System.out.println(num);
        }
    }
}
```

## When to Use ArrayDeque?

- When **fast insertions and deletions** are needed at both ends.
- When implementing **stacks and queues** efficiently.
- When **ordering matters** and elements need to be accessed from both ends.
- When **better performance** is required compared to `LinkedList` for queue operations.
