## **How to Approach Sliding Window Problems?**  
Sliding Window is a powerful technique used to efficiently **process subarrays or substrings** in problems where a brute force approach would be too slow.

### **📌 When to Use Sliding Window?**
1. **Finding the longest/shortest subarray or substring** that satisfies a condition.
2. **Subarray with a given sum, product, or unique elements**.
3. **Problems that involve a continuous range of elements**.
4. **Optimizing problems with a moving range instead of recomputing from scratch**.

---
## **🧠 Step-by-Step Approach**
1️⃣ **Define the problem clearly.**  
   - Are we looking for **maximum/minimum length**?  
   - Are we dealing with **a sum, product, or unique elements**?  

2️⃣ **Decide between a Fixed or Variable Window.**
   - **Fixed Window Size** → Given length **k**, slide the window **step-by-step**.  
   - **Variable Window Size** → Expand/shrink dynamically to satisfy conditions.  

3️⃣ **Use Two Pointers (Left and Right).**
   - `right` expands the window.  
   - `left` shrinks the window when needed.  

4️⃣ **Apply conditions while moving pointers.**
   - Maintain required **sum, frequency, count, or unique elements**.
   - Adjust `left` when the condition is **violated**.

---
## **🔹 Types of Sliding Window Problems**
Let's break down different types of **Sliding Window** problems with examples.

---

### **1️⃣ Fixed Size Sliding Window**
**🔹 Problem Type:** Maximum/Minimum of a fixed-length subarray.  
**✅ Key Idea:** Maintain a window of size `k`, slide it across the array.

#### **Example 1: Maximum Sum of Subarray of Size K**
**📌 Problem:** Given an array `arr` and an integer `k`, find the **maximum sum** of any contiguous subarray of size `k`.  
**🔹 Approach:**
- First, compute the sum of the first `k` elements.
- Slide the window by removing the first element (`left++`) and adding the next element (`right++`).

```python
def max_subarray_sum(arr, k):
    max_sum, curr_sum = 0, sum(arr[:k])  # First window sum
    for i in range(k, len(arr)):
        curr_sum += arr[i] - arr[i - k]  # Slide window
        max_sum = max(max_sum, curr_sum)
    return max_sum
```
**🕒 Complexity:** **O(N)** (Instead of O(N*K) brute force)

---

### **2️⃣ Variable Size Sliding Window**
**🔹 Problem Type:** Find the **smallest or largest subarray** that meets a condition.  
**✅ Key Idea:** Expand the window (`right++`), and shrink (`left++`) when the condition is violated.

#### **Example 2: Smallest Subarray with Sum ≥ S**
**📌 Problem:** Given an array `arr` and a number `S`, find the **smallest contiguous subarray** whose sum is at least `S`.  
**🔹 Approach:**
- Expand `right` to **increase sum**.
- When sum **≥ S**, shrink `left` to find the smallest valid subarray.

```python
def min_subarray_length(arr, S):
    left, curr_sum, min_length = 0, 0, float('inf')
    for right in range(len(arr)):
        curr_sum += arr[right]  # Expand window
        while curr_sum >= S:
            min_length = min(min_length, right - left + 1)
            curr_sum -= arr[left]  # Shrink window
            left += 1
    return min_length if min_length != float('inf') else 0
```
**🕒 Complexity:** **O(N)** (Instead of O(N²) brute force)

---

### **3️⃣ Longest Substring with Unique Characters**
**🔹 Problem Type:** Find the **longest substring** that meets a given condition.  
**✅ Key Idea:** Use a **set or dictionary** to track elements, expanding until a duplicate is found.

#### **Example 3: Longest Substring Without Repeating Characters**
**📌 Problem:** Find the length of the **longest substring without repeating characters**.  
**🔹 Approach:**
- Expand `right`, adding characters to a **set**.
- If a duplicate is found, **remove characters from the left** until valid.

```python
def longest_unique_substring(s):
    char_set = set()
    left, max_length = 0, 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])  # Remove leftmost character
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length
```
**🕒 Complexity:** **O(N)** (Instead of O(N²) brute force)

---

### **4️⃣ Count Occurrences with Sliding Window**
**🔹 Problem Type:** Find the **count of occurrences** of a pattern in a large dataset.  
**✅ Key Idea:** Maintain a **frequency map** and slide the window.

#### **Example 4: Find All Anagrams of a Pattern in a String**
**📌 Problem:** Given two strings `s` and `p`, find **all starting indices** of `p`'s anagrams in `s`.  
**🔹 Approach:**
- Maintain a **frequency map** for `p` and track characters in `s` using a window.
- If both maps match, store the index.

```python
from collections import Counter

def find_anagrams(s, p):
    p_count, s_count = Counter(p), Counter(s[:len(p)-1])
    result, left = [], 0
    for right in range(len(p)-1, len(s)):
        s_count[s[right]] += 1  # Expand window
        if s_count == p_count:
            result.append(left)
        s_count[s[left]] -= 1  # Shrink window
        if s_count[s[left]] == 0:
            del s_count[s[left]]
        left += 1
    return result
```
**🕒 Complexity:** **O(N)** (Instead of O(N*M) brute force)

---

## **🔹 Sliding Window Template**
Many problems follow this template:

```python
def sliding_window(arr, condition):
    left, curr_result = 0, 0
    for right in range(len(arr)):
        # Expand window
        # Add arr[right] to the current result
        
        while condition_violated:
            # Shrink window from left
            # Remove arr[left] from the current result
            left += 1
            
        # Update answer (e.g., max/min length, sum)
    return result
```

---

## **🔹 When to Expand vs. Shrink?**
| Scenario | Expand (`right++`) | Shrink (`left++`) |
|----------|------------------|------------------|
| **Find longest subarray** | Until constraint is met | If constraint breaks |
| **Find shortest subarray** | Until sum condition met | To minimize window |
| **Find all valid substrings** | Until invalid character | Remove invalid characters |

---

## **🔹 Summary**
| Problem Type | Approach |
|-------------|---------|
| **Fixed Size Window** | Slide window step by step, keep max/min result |
| **Variable Window (Longest/Shortest Subarray)** | Expand `right`, shrink `left` when condition is met |
| **Unique Characters (Longest Substring)** | Use a `set` to track duplicates |
| **Count-based problems (Anagrams, Frequency)** | Use a `hashmap` for tracking |

---
## **🔹 Final Thoughts**
- **Sliding Window saves time** by avoiding unnecessary recomputation.
- **Decide between Fixed or Variable window size**.
- **Use Two Pointers (`left` and `right`) to dynamically adjust the window**.
- **Use Data Structures** (`Set`, `HashMap`, `Deque`) for efficient tracking.

Would you like me to explain any of these concepts in **greater detail** with **diagrams**? 🚀