
# LEETCODE - 907 

class Solution:
    def sumSubarrayMins(self, arr):
        n = len(arr)

        MOD = 10**9 + 7
        prev_smaller = [-1] * n
        next_smaller = [n] * n
        
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            next_smaller[i] = stack[-1] if stack else n
            stack.append(i)
        
        total_sum = 0
        for i in range(n):
            count = (i - prev_smaller[i]) * (next_smaller[i] - i)
            total_sum += arr[i] * count
            total_sum %= MOD
        
        return total_sum

if __name__ == '__main__':
	
	arr = [71,55,82,55]

	obj = Solution()
	answer = obj.sumSubarrayMins(arr)

	print(answer)