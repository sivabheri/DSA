#User function Template for python3
import sys
class Solution:
    def sumClosest(self, arr, target):
        # code here
        arr.sort()
        return self.approach1(arr,target)
    
    def approach1(self,arr,target) :
        n = len(arr)
        
        l,r = 0, n-1
        ans = []
        mini = sys.maxsize
        while l<r :
            
            res = arr[l]+arr[r]
            # when it will be closesest if res> target or < targest the difference must be minimum
            
            if abs(res-target) < mini:
                mini = abs(res-target)
                ans = [arr[l],arr[r]]
                
            # when their sum is > target or < target
            if res > target:
                r -= 1
            elif res < target:
                
                l += 1
            else:
                return ans
        return ans[-1]

if __name__ == '__main__':
    
    obj = Solution()
    arr = [1,2,3,4,5,6]
    k = 10
    ans = obj.sumClosest(arr,k)
    print(ans)    