# HashMap in Java

## Overview

- `HashMap` is a part of `java.util` package.
- Stores elements as **key-value pairs**.
- Allows **null keys** and **multiple null values**.
- Does **not maintain order** of insertion.
- Provides **O(1) average time complexity** for `put()`, `get()`, and `remove()` operations.

## Import Statement

```java
import java.util.HashMap;
```

## Initialization

```java
HashMap<KeyType, ValueType> hashMap = new HashMap<>();
```

## Operations

### 1. Adding Elements

```java
hashMap.put(key, value);
```

### 2. Accessing Elements

```java
ValueType value = hashMap.get(key);
```

### 3. Checking If a Key Exists

```java
boolean containsKey = hashMap.containsKey(key);
```

### 4. Checking If a Value Exists

```java
boolean containsValue = hashMap.containsValue(value);
```

### 5. Removing an Element

```java
hashMap.remove(key);
```

### 6. Getting the Size

```java
int size = hashMap.size();
```

### 7. Checking If Empty

```java
boolean isEmpty = hashMap.isEmpty();
```

### 8. Iterating Over a HashMap

#### Using `entrySet()` (Recommended for both key and value)

```java
for (Map.Entry<KeyType, ValueType> entry : hashMap.entrySet()) {
    System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
}
```

#### Using `keySet()` (Iterating over keys only)

```java
for (KeyType key : hashMap.keySet()) {
    System.out.println("Key: " + key);
}
```

#### Using `values()` (Iterating over values only)

```java
for (ValueType value : hashMap.values()) {
    System.out.println("Value: " + value);
}
```

#### Using an Iterator

```java
Iterator<Map.Entry<KeyType, ValueType>> iterator = hashMap.entrySet().iterator();
while (iterator.hasNext()) {
    Map.Entry<KeyType, ValueType> entry = iterator.next();
    System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
}
```

### 9. Removing All Elements

```java
hashMap.clear();
```

## Example Program

```java
import java.util.HashMap;
import java.util.Map;

public class HashMapExample {
    public static void main(String[] args) {
        // Initialize HashMap
        HashMap<Integer, String> hashMap = new HashMap<>();
      
        // Adding elements
        hashMap.put(1, "Apple");
        hashMap.put(2, "Banana");
        hashMap.put(3, "Cherry");
      
        // Accessing an element
        System.out.println("Value for key 2: " + hashMap.get(2));
      
        // Checking if a key exists
        System.out.println("Contains key 3? " + hashMap.containsKey(3));
      
        // Iterating over HashMap
        for (Map.Entry<Integer, String> entry : hashMap.entrySet()) {
            System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
        }
      
        // Removing an element
        hashMap.remove(1);
      
        // Clearing HashMap
        hashMap.clear();
        System.out.println("Is HashMap empty? " + hashMap.isEmpty());
    }
}
```

## When to Use HashMap?

- When you need **fast lookups** based on a key.
- If **ordering is not important**.
- When you need **unique keys** mapping to values.
