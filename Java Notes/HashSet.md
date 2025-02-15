# HashSet in Java

## Overview

- `HashSet` is an implementation of the `Set` interface that **does not allow duplicate elements**.
- Uses **hashing** for storing elements, ensuring **constant-time performance (O(1))** for add, remove, and contains operations.
- Does **not maintain insertion order**.

## Import Statement

```java
import java.util.HashSet;
```

## Initialization

```java
HashSet<Type> hashSet = new HashSet<>();
```

## Operations

### 1. Adding Elements

```java
hashSet.add(element);
```

### 2. Checking if an Element Exists

```java
boolean exists = hashSet.contains(element);
```

### 3. Removing Elements

```java
hashSet.remove(element);
```

### 4. Getting Size

```java
int size = hashSet.size();
```

### 5. Checking if Empty

```java
boolean isEmpty = hashSet.isEmpty();
```

### 6. Iterating Over Elements

```java
for (Type x : hashSet) {
    System.out.println(x);
}
```

Or using an iterator:

```java
Iterator<Type> it = hashSet.iterator();
while (it.hasNext()) {
    System.out.println(it.next());
}
```

### 7. Removing All Elements

```java
hashSet.clear();
```

### 8. Cloning a HashSet

```java
HashSet<Type> clonedSet = (HashSet<Type>) hashSet.clone();
```

### 9. Converting HashSet to Array

```java
Type[] array = hashSet.toArray(new Type[0]);
```

## Example Program

```java
import java.util.HashSet;

public class HashSetExample {
    public static void main(String[] args) {
        // Initialize HashSet
        HashSet<Integer> hashSet = new HashSet<>();
      
        // Adding elements
        hashSet.add(10);
        hashSet.add(20);
        hashSet.add(30);
        hashSet.add(40);
        hashSet.add(20); // Duplicate, will not be added
      
        // Checking if an element exists
        System.out.println("Contains 20? " + hashSet.contains(20));
      
        // Removing an element
        hashSet.remove(30);
      
        // Iterating over HashSet
        System.out.println("HashSet elements:");
        for (int num : hashSet) {
            System.out.println(num);
        }
      
        // Getting size
        System.out.println("Size of HashSet: " + hashSet.size());
      
        // Clearing the HashSet
        hashSet.clear();
        System.out.println("Is HashSet empty? " + hashSet.isEmpty());
    }
}
```

## For Set Operations

```java
// such as Union, Intersection and Difference operations 

import java.util.*;

// Main class 
public class SetExample {
  
    // Main driver method 
    public static void main(String args[])
    {
        // Creating an object of Set class 
        // Declaring object of Integer type 
        Set<Integer> a = new HashSet<Integer>();
  
        // Adding all elements to List 
        a.addAll(Arrays.asList(
            new Integer[] { 1, 3, 2, 4, 8, 9, 0 }));
  
      // Again declaring object of Set class
      // with reference to HashSet
        Set<Integer> b = new HashSet<Integer>();
  
      b.addAll(Arrays.asList(
            new Integer[] { 1, 3, 7, 5, 4, 0, 7, 5 }));

  
        // To find union
        Set<Integer> union = new HashSet<Integer>(a);
        union.addAll(b);
        System.out.print("Union of the two Set");
        System.out.println(union);

        // To find intersection
        Set<Integer> intersection = new HashSet<Integer>(a);
        intersection.retainAll(b);
        System.out.print("Intersection of the two Set");
        System.out.println(intersection);

        // To find the symmetric difference
        Set<Integer> difference = new HashSet<Integer>(a);
        difference.removeAll(b);
        System.out.print("Difference of the two Set");
        System.out.println(difference);
    }
}

```

## When to Use HashSet?

- When you need **fast lookup, insertion, and deletion** (O(1) time complexity).
- If you **don’t need ordering** of elements.
- When **duplicate elements are not allowed**.
