# LEETCODE - 347 
# There is a better approach that takes linear time
from collections import Counter
from heapq import heappush, heappop , heappushpop
class Solution:
    def topKFrequent(self, nums, k):
        
        freq = Counter(nums)

        heap = []

        for num,cnt in freq.items():

            if len(heap) < k:
                heappush(heap,(cnt,num))
            else:
                heappushpop(heap,(cnt,num))

        return [h[1] for h in heap]

        # Time: (N + N log(k))  Space: k

if __name__ == '__main__':
    
    obj = Solution()

    arr = [int(i) for i in input().strip('[]').split(',')] #[1,1,1,2,2,3]
    k = int(input()) #2
    print(f'Top K Frequent Elements are : {obj.topKFrequent(arr,k)}')