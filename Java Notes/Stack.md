# Stack in Java

## Overview
- `Stack` is a **Last-In-First-Out (LIFO)** data structure.
- It extends `Vector` and provides additional methods for stack operations.
- It is **synchronized** (thread-safe).

## Import Statement
```java
import java.util.Stack;
```

## Initialization
```java
Stack<Type> stack = new Stack<>();
```

## Operations

### 1. Pushing Elements (Adding to Stack)
```java
stack.push(element);
```

### 2. Popping Elements (Removing from Stack)
```java
Type element = stack.pop();
```

### 3. Peeking (Getting Top Element Without Removing)
```java
Type topElement = stack.peek();
```

### 4. Checking if Stack is Empty
```java
boolean isEmpty = stack.isEmpty();
```

### 5. Searching for an Element (Returns Position)
```java
int position = stack.search(element);
```

### 6. Iterating Over Stack Elements
```java
for (Type x : stack) {
    System.out.println(x);
}
```
Or using an iterator:
```java
Iterator<Type> it = stack.iterator();
while (it.hasNext()) {
    System.out.println(it.next());
}
```

### 7. Getting Stack Size
```java
int size = stack.size();
```

### 8. Clearing the Stack
```java
stack.clear();
```

## Example Program
```java
import java.util.Stack;

public class StackExample {
    public static void main(String[] args) {
        // Initialize Stack
        Stack<Integer> stack = new Stack<>();
        
        // Pushing elements
        stack.push(10);
        stack.push(20);
        stack.push(30);
        
        // Peeking top element
        System.out.println("Top element: " + stack.peek());
        
        // Popping elements
        System.out.println("Popped element: " + stack.pop());
        
        // Checking if stack is empty
        System.out.println("Is stack empty? " + stack.isEmpty());
        
        // Iterating over stack
        System.out.println("Stack elements:");
        for (int num : stack) {
            System.out.println(num);
        }
    }
}
```

## When to Use Stack?
- When you need **Last-In-First-Out (LIFO)** behavior.
- If you require a thread-safe stack implementation (as `Stack` is synchronized).
- For operations like **undo/redo**, **backtracking**, **expression evaluation**, etc.
