# TreeMap in Java

## Overview

- `TreeMap` is a part of `java.util` package.
- Implements `NavigableMap`, maintaining keys in **sorted order**.
- Uses a **Red-Black Tree** for storing key-value pairs.
- **Does not allow null keys** but allows multiple null values.
- Provides **O(log n) time complexity** for insertions, deletions, and lookups.

## Import Statement

```java
import java.util.TreeMap;
```

## Initialization

```java
TreeMap<KeyType, ValueType> treeMap = new TreeMap<>();
```

## Operations

### 1. Adding Elements

```java
treeMap.put(key, value);
```

### 2. Accessing Elements

```java
ValueType value = treeMap.get(key);
```

### 3. Removing an Element

```java
treeMap.remove(key);
```

### 4. Checking If a Key Exists

```java
boolean containsKey = treeMap.containsKey(key);
```

### 5. Checking If a Value Exists

```java
boolean containsValue = treeMap.containsValue(value);
```

### 6. Getting First and Last Key

```java
KeyType firstKey = treeMap.firstKey();
KeyType lastKey = treeMap.lastKey();
```

### 7. Iterating Over a TreeMap

```java
for (Map.Entry<KeyType, ValueType> entry : treeMap.entrySet()) {
    System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
}
```

### 8. Clearing the TreeMap

```java
treeMap.clear();
```

## Example Program

```java
import java.util.TreeMap;
import java.util.Map;

public class TreeMapExample {
    public static void main(String[] args) {
        // Initialize TreeMap
        TreeMap<Integer, String> treeMap = new TreeMap<>();
      
        // Adding elements
        treeMap.put(1, "Apple");
        treeMap.put(3, "Cherry");
        treeMap.put(2, "Banana");
      
        // Iterating over TreeMap
        for (Map.Entry<Integer, String> entry : treeMap.entrySet()) {
            System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
        }
    }
}
```

## When to Use TreeMap?

- When you need **sorted keys**.
- When **ordering is important**.
- When you require **fast access to the first or last key**.
