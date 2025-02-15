# Vector in Java

## Overview
- `Vector` is a **resizable** array similar to `ArrayList`, but it is **synchronized** (thread-safe).
- Allows **duplicate elements** and maintains **insertion order**.
- Slower than `ArrayList` due to synchronization.

## Import Statement
```java
import java.util.Vector;
```

## Initialization
```java
Vector<Type> vector = new Vector<>();
```
Or with an initial capacity:
```java
Vector<Type> vector = new Vector<>(capacity);
```

## Operations

### 1. Adding Elements
```java
vector.add(element);
vector.add(index, element);
```

### 2. Accessing Elements
```java
Type element = vector.get(index);
```

### 3. Getting Size
```java
int size = vector.size();
```

### 4. Checking if Empty
```java
boolean isEmpty = vector.isEmpty();
```

### 5. Checking if Element Exists
```java
boolean exists = vector.contains(element);
```

### 6. Removing Elements
```java
vector.remove(index);
vector.remove(element); // First occurrence
```

### 7. Updating an Element
```java
vector.set(index, newElement);
```

### 8. Iterating Over Elements
```java
for (Type x : vector) {
    System.out.println(x);
}
```
Or using an iterator:
```java
Iterator<Type> it = vector.iterator();
while (it.hasNext()) {
    System.out.println(it.next());
}
```

### 9. Getting Index of an Element
```java
int index = vector.indexOf(element);
int lastIndex = vector.lastIndexOf(element);
```

### 10. Sublist Extraction
```java
List<Type> subVector = vector.subList(fromIndex, toIndex);
```

### 11. Removing a Collection of Elements
```java
vector.removeAll(anotherCollection);
```

### 12. Clearing the Vector
```java
vector.clear();
```

### 13. Cloning a Vector
```java
Vector<Type> clonedVector = (Vector<Type>) vector.clone();
```

### 14. Converting Vector to Array
```java
Type[] array = vector.toArray(new Type[0]);
```

### 15. Sorting a Vector
```java
Collections.sort(vector);
```

## Example Program
```java
import java.util.Vector;
import java.util.Collections;

public class VectorExample {
    public static void main(String[] args) {
        // Initialize Vector
        Vector<Integer> vector = new Vector<>();
        
        // Adding elements
        vector.add(10);
        vector.add(20);
        vector.add(30);
        
        // Accessing elements
        System.out.println("Element at index 1: " + vector.get(1));
        
        // Removing an element
        vector.remove(1);
        
        // Checking if an element exists
        System.out.println("Vector contains 20? " + vector.contains(20));
        
        // Iterating over the vector
        System.out.println("Vector elements:");
        for (int num : vector) {
            System.out.println(num);
        }
        
        // Sorting
        vector.add(5);
        vector.add(25);
        Collections.sort(vector);
        
        System.out.println("Sorted Vector: " + vector);
    }
}
```

## When to Use Vector?
- When **thread safety** is required (as `Vector` is synchronized).
- If you need **dynamic resizing** and synchronized access.
- When working in a **multithreaded environment** where multiple threads access the collection.
