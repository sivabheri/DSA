# TreeSet in Java

## Overview

- `TreeSet` is an implementation of the `NavigableSet` interface based on a **Red-Black Tree**.
- It **does not allow duplicate elements**.
- Maintains elements in **sorted order** (natural ordering or a custom comparator).
- Provides **logarithmic time (O(log n))** for basic operations like add, remove, and contains.

## Import Statement

```java
import java.util.TreeSet;
```

## Initialization

```java
TreeSet<Type> treeSet = new TreeSet<>();
```

Or using a custom comparator:

```java
TreeSet<Type> treeSet = new TreeSet<>(Comparator.comparing(Type::someMethod));
```

## Operations

### 1. Adding Elements

```java
treeSet.add(element);
```

### 2. Checking if an Element Exists

```java
boolean exists = treeSet.contains(element);
```

### 3. Removing Elements

```java
treeSet.remove(element);
```

### 4. Getting Size

```java
int size = treeSet.size();
```

### 5. Checking if Empty

```java
boolean isEmpty = treeSet.isEmpty();
```

### 6. Iterating Over Elements (Sorted Order)

```java
for (Type x : treeSet) {
    System.out.println(x);
}
```

Or using an iterator:

```java
Iterator<Type> it = treeSet.iterator();
while (it.hasNext()) {
    System.out.println(it.next());
}
```

### 7. Removing All Elements

```java
treeSet.clear();
```

### 8. Getting First and Last Elements

```java
Type first = treeSet.first();
Type last = treeSet.last();
```

### 9. Subset Operations

```java
SortedSet<Type> headSet = treeSet.headSet(element); // Elements less than `element`
SortedSet<Type> tailSet = treeSet.tailSet(element); // Elements greater than or equal to `element`
SortedSet<Type> subSet = treeSet.subSet(startElement, endElement); // Range
```

### 10. Cloning a TreeSet

```java
TreeSet<Type> clonedSet = (TreeSet<Type>) treeSet.clone();
```

### 11. Converting TreeSet to Array

```java
Type[] array = treeSet.toArray(new Type[0]);
```

## Example Program

```java
import java.util.TreeSet;

public class TreeSetExample {
    public static void main(String[] args) {
        // Initialize TreeSet
        TreeSet<Integer> treeSet = new TreeSet<>();
      
        // Adding elements
        treeSet.add(50);
        treeSet.add(20);
        treeSet.add(40);
        treeSet.add(10);
        treeSet.add(30);
      
        // Display elements (sorted)
        System.out.println("TreeSet elements: " + treeSet);
      
        // Checking if an element exists
        System.out.println("Contains 20? " + treeSet.contains(20));
      
        // Removing an element
        treeSet.remove(30);
      
        // Getting first and last elements
        System.out.println("First element: " + treeSet.first());
        System.out.println("Last element: " + treeSet.last());
      
        // Getting a subset
        System.out.println("Elements less than 40: " + treeSet.headSet(40));
      
        // Clearing the TreeSet
        treeSet.clear();
        System.out.println("Is TreeSet empty? " + treeSet.isEmpty());
    }
}
```

## When to Use TreeSet?

- When you need **sorted order** of elements.
- If **duplicate elements are not allowed**.
- When you need **efficient range queries** (subset, headSet, tailSet).
- If you need **logarithmic time complexity (O(log n))** for add, remove, and search operations.
