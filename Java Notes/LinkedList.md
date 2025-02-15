# LinkedList in Java

## Overview

- `LinkedList` is a **doubly linked list** implementation of the `List` and `Deque` interfaces.
- Allows **duplicate elements** and maintains **insertion order**.
- Provides **efficient insertions and deletions** compared to `ArrayList`.

## Import Statement

```java
import java.util.LinkedList;
```

## Initialization

```java
LinkedList<Type> linkedList = new LinkedList<>();
```

Or using `List` reference:

```java
List<Type> linkedList = new LinkedList<>();
```

## Operations

### 1. Adding Elements

```java
linkedList.add(element);
linkedList.add(index, element);
linkedList.addFirst(element);
linkedList.addLast(element);
```

### 2. Accessing Elements

```java
Type firstElement = linkedList.getFirst();
Type lastElement = linkedList.getLast();
Type element = linkedList.get(index);
```

### 3. Getting Size

```java
int size = linkedList.size();
```

### 4. Checking if Empty

```java
boolean isEmpty = linkedList.isEmpty();
```

### 5. Checking if Element Exists

```java
boolean exists = linkedList.contains(element);
```

### 6. Removing Elements

```java
linkedList.remove(index);
linkedList.remove(element); // Removes first occurrence
linkedList.removeFirst();
linkedList.removeLast();
```

### 7. Updating an Element

```java
linkedList.set(index, newElement);
```

### 8. Iterating Over Elements

```java
for (Type x : linkedList) {
    System.out.println(x);
}
```

Or using an iterator:

```java
Iterator<Type> it = linkedList.iterator();
while (it.hasNext()) {
    System.out.println(it.next());
}
```

### 9. Getting Index of an Element

```java
int index = linkedList.indexOf(element);
int lastIndex = linkedList.lastIndexOf(element);
```

### 10. Sublist Extraction

```java
List<Type> subList = linkedList.subList(fromIndex, toIndex);
```

### 11. Removing a Collection of Elements

```java
linkedList.removeAll(anotherCollection);
```

### 12. Clearing the LinkedList

```java
linkedList.clear();
```

### 13. Cloning a LinkedList

```java
LinkedList<Type> clonedList = (LinkedList<Type>) linkedList.clone();
```

### 14. Converting LinkedList to Array

```java
Type[] array = linkedList.toArray(new Type[0]);
```

### 15. Sorting a LinkedList

```java
Collections.sort(linkedList);
```

## Example Program

```java
import java.util.LinkedList;
import java.util.Collections;

public class LinkedListExample {
    public static void main(String[] args) {
        // Initialize LinkedList
        LinkedList<Integer> linkedList = new LinkedList<>();
      
        // Adding elements
        linkedList.add(10);
        linkedList.add(20);
        linkedList.add(30);
        linkedList.addFirst(5);
        linkedList.addLast(40);
      
        // Accessing elements
        System.out.println("First element: " + linkedList.getFirst());
        System.out.println("Last element: " + linkedList.getLast());
      
        // Removing elements
        linkedList.removeFirst();
        linkedList.removeLast();
      
        // Checking if LinkedList is empty
        System.out.println("Is LinkedList empty? " + linkedList.isEmpty());
      
        // Iterating over LinkedList
        System.out.println("LinkedList elements:");
        for (int num : linkedList) {
            System.out.println(num);
        }
      
        // Sorting
        linkedList.add(15);
        linkedList.add(25);
        Collections.sort(linkedList);
      
        System.out.println("Sorted LinkedList: " + linkedList);
    }
}
```

## When to Use LinkedList?

- When you need **frequent insertions and deletions**.
- If you require **constant-time insertions/removals** from the beginning/middle.
- When you don’t need **frequent random access** (use `ArrayList` for that).
