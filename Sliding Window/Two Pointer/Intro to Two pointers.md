<!-- Two pointers Approach  -->

## **Two Pointers Approach in Problem Solving**
The **two pointers** technique is a powerful algorithmic approach often used to optimize problems involving arrays, strings, and linked lists. The idea is to use two indices (or pointers) to traverse data in a way that reduces time complexity, often from **O(N²) to O(N)**.

---

## **Identifying Two Pointer Problems**
A problem is likely to be solved using **two pointers** if:
1. **Sorted Array / List / String:** If the given data is sorted, two pointers can help optimize searching.
2. **Pair or Subarray with Given Condition:** When asked to find pairs, triplets, or subarrays with a given sum, difference, or product.
3. **Comparing Elements from Both Ends:** When you need to process elements from both ends of an array (e.g., palindromes, partitioning, etc.).
4. **Merging or Comparing Two Lists:** Useful when merging two sorted arrays or checking subsequence matches.
5. **Sliding Window Optimization:** Some sliding window problems can be optimized using two pointers.

---

## **Types of Two Pointer Problems - Based on Placement of Pointers**

### **1. Opposite Direction Two Pointers**
- **Idea:** Start one pointer from the left and the other from the right and move towards each other based on conditions.
- **Use Cases:** 
  - Finding a pair with a target sum
  - Checking if an array is a palindrome
  - Trapping rainwater problem
- **Examples:**
  - **Two Sum (Sorted Array)** → Find two numbers that add up to a target sum.
  - **Valid Palindrome** → Check if a string is a palindrome.
  - **Container with Most Water** → Maximize the area between two lines.

---

### **2. Same Direction Two Pointers (Slow & Fast)**
- **Idea:** One pointer moves faster than the other to process or filter data efficiently.
- **Use Cases:** 
  - Removing duplicates from sorted array
  - Detecting a cycle in a linked list
  - Partitioning an array
- **Examples:**
  - **Remove Duplicates from Sorted Array** → Shift elements to maintain unique values.
  - **Cycle Detection in Linked List (Floyd’s Algorithm)** → Detect a loop in a linked list.
  - **Sort Colors (Dutch National Flag Problem)** → Sort 0s, 1s, and 2s in linear time.

---

### **3. Merging Two Lists**
- **Idea:** Use two pointers to merge two sorted arrays or find common elements efficiently.
- **Use Cases:**
  - Merging sorted arrays
  - Finding intersections in two sorted lists
  - Finding union/difference of two lists
- **Examples:**
  - **Merge Two Sorted Arrays (without extra space)**
  - **Intersection of Two Sorted Arrays**
  - **Finding K-th smallest element in two sorted arrays**

---

### **4. Subarray/Substring with a Given Condition (Sliding Window)**
- **Idea:** Expand and contract a window to satisfy a condition while keeping track of the optimal answer.
- **Use Cases:**
  - Finding the smallest subarray with a given sum
  - Finding the longest substring without repeating characters
  - Minimum window substring matching a pattern
- **Examples:**
  - **Longest Substring Without Repeating Characters**
  - **Minimum Window Substring**
  - **Smallest Subarray with a Sum Greater than Target**

---

### **5. Partitioning / Rearranging Elements**
- **Idea:** Use two pointers to separate elements based on a condition.
- **Use Cases:**
  - Segregating even and odd numbers
  - Moving all zeros to the end
  - Partitioning a linked list
- **Examples:**
  - **Move Zeros to End**
  - **Segregate Even and Odd Numbers**
  - **Partition Linked List around a Pivot**


---

## **Practice Problems (Leetcode)**
1. **Two Sum - Sorted Array** (Leetcode #167)  
2. **Valid Palindrome** (Leetcode #125)  
3. **Container With Most Water** (Leetcode #11)  
4. **Trapping Rain Water** (Leetcode #42)  
5. **Remove Duplicates from Sorted Array** (Leetcode #26)  
6. **Linked List Cycle Detection** (Leetcode #141)  
7. **Merge Two Sorted Lists** (Leetcode #21)  
8. **Longest Substring Without Repeating Characters** (Leetcode #3)  
9. **Minimum Window Substring** (Leetcode #76)  
10. **Move Zeros to End** (Leetcode #283)  
