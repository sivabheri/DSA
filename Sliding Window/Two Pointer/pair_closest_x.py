# Find the pair which is closest to given element

'''
Given two sorted arrays and an interger X,
we need to find the values of pair whoses sum is close to X.

Input : N = 4, M = 4
arr[ ] = {1, 4, 5, 7}
brr[ ] = {10, 20, 30, 40} 
X = 32
Output : 
1, 30
Explanation:
The closest pair whose sum is closest
to 32 is {1, 30} = 31.

Intution :

Approach 1:
While sovling sum with target problems we need to use two pointer techniques.
Placement of pointers keep one pointer at beginnig of one array ane end of other array.
Move the pointers while checking the condition.

Approach 2:

Travese array1  and do binary_seach on (target - arr1[i]) in array 2. ie. pos = BS(arr2, target-arr[i])
now check if element is in range of array 2-> if pos < m: then update the minimum difference ,
also check if pos is valid pos > 0 , again update the minimum difference 
'''
import sys
class Solution:
    def printClosest1(self,arr, brr, n, m, x) : 
    
        # take 2 pointer one at begining and other at the end
        l,r = 0, m-1
        
        ans = (0,0)
        
        mini = sys.maxsize
        
        # as long as l < n and  r > -1 we keep on doings
        while (l<n and r>=0) :
            
            # we need to find the closest val of sum < x :
            # so if the sum exceeds x we do r -- else l ++
            # but we need the value of sum which is close to x
            if abs(arr[l] + brr[r] - x) < mini:
                mini = abs(arr[l]+brr[r]-x)
                ans = (arr[l],brr[r])
            if  arr[l] + brr[r] > x:
                r -= 1
            else :
                l += 1
        return ans

    def binary_search(self, brr, target):
        low, high = 0, len(brr) - 1
        best = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if brr[mid] < target:
                best = mid  # Update best to the current mid
                low = mid + 1  # Move right
            else:
                high = mid - 1  # Move left
        
        return best  # Return the index of the closest element less than target

    def printClosest2(self, arr, brr, n, m, x):
        ans = (0, 0)
        mini = sys.maxsize
        
        # Iterate through each element in arr
        for i in range(n):
            # Calculate the complement needed to reach x
            target = x - arr[i]
            
            # Perform binary search to find the closest element in brr
            pos = self.binary_search(brr, target)
            
            # Check the position found by binary search
            if pos != -1:  # Check if a valid position was found
                sum_with_pos = arr[i] + brr[pos]
                if abs(sum_with_pos - x) < mini:
                    mini = abs(sum_with_pos - x)
                    ans = (arr[i], brr[pos])
            
            if pos + 1 < m:  # Check the next element if it exists
                sum_with_next_pos = arr[i] + brr[pos + 1]
                if abs(sum_with_next_pos - x) < mini:
                    mini = abs(sum_with_next_pos - x)
                    ans = (arr[i], brr[pos + 1])
        
        return ans

for _ in range(0,int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    brr = list(map(int, input().strip().split()))
    x = int(input())
    ob = Solution()
    ans = ob.printClosest2(arr, brr, n, m, x)
    print(abs(ans[0]+ans[1] - x))
    print("~")