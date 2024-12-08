#Next Permutation
'''-----------------------------

2 1 5 4 3 0 0 -> 2 3 0 0 1 4 5

ind= -1
from n-1 to 0 find element`s ind : i < i+1 

0 < 0  x
3 < 0  x
4 < 3  x
5 < 4  x
1 < 4  [ True ] -> ind = at(1)

# if not found : ind == -1 : Rotate whole array

from n-1 to ind :
	
find element that is just greater than ele at(ind)

0 > 1 x
0 > 1 x
3 > 1 [true] -> swap(I,ind)

arr = 2 3 4 1 0 0

from ind+1 to n reverse the elements

arr = 2 3 '0 0 1 4

-------------------------------------'''

class Solution:
    def nextPermutation(self, nums) :
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)  
        ind = -1  
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break

        if ind == -1:
            nums.reverse()
            return nums
        print(f"\nBreak point at element : {nums[ind]} and index : {ind} \n")
        
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break
        print(f"Array after swapping larget element on right half of ind, with @ind : \n {nums}")

        nums[ind + 1 :] = reversed(nums[ind + 1 :])

        return nums

if __name__ == '__main__':
	
	obj = Solution()

	arr = [int(i) for i in input().split()]

	print("\nThe Next Permutation is : ",obj.nextPermutation(arr))
