# LEETCODE 2136 - HARD
# asked in Google, Amazon , MicroSoft and Adobe

''' 
your are given tow arrays , plantTime and growTime,
planTime[i] = time taken by ith seed to plant,
growTime[i] = time taken for ith seed to grow

Conditons: No two seeds should be planted on the same day,

Output: Return the earliest time(min time) for all seeds to bloom.

example 1:
Input: plantTime = [1,4,3], growTime = [2,3,1]
Output: 9
Explanation: 
On day 0, plant the 0th seed. The seed grows for 2 full days and blooms on day 3.
On days 1, 2, 3, and 4, plant the 1st seed. The seed grows for 3 full days and blooms on day 8.
On days 5, 6, and 7, plant the 2nd seed. The seed grows for 1 full day and blooms on day 9.
Thus, on day 9, all the seeds are blooming.

Input: plantTime = [1,2,3,2], growTime = [2,1,2,1]
Output: 9
Explanation:
On day 1, plant the 0th seed. The seed grows for 2 full days and blooms on day 4.
On days 0 and 3, plant the 1st seed. The seed grows for 1 full day and blooms on day 5.
On days 2, 4, and 5, plant the 2nd seed. The seed grows for 2 full days and blooms on day 8.
On days 6 and 7, plant the 3rd seed. The seed grows for 1 full day and blooms on day 9.
Thus, on day 9, all the seeds are blooming.

'''
from typing import List
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        # sort both the arrays according to their growTimes
        n = len(plantTime)
        plants = []
        for i in range(n):
            plants.append((plantTime[i],growTime[i]))

        plants.sort(key=lambda x:x[1],reverse=True)

        # Finsh one plant(seed) and find out how much time it takes to bloom  = Planting time(startday+ planTime) +   growTime
        # then start other plant which means no two seed should be planted on the same day
        # This can be done by tracking the previous seed's end planted day,
        # so, new seed can be sown on prevPlant end day(plantTime) + 1
        # for each seed keep track of Maxdays takes return the highest value which is our answer
        maxTime = 0
        prevPlantTime = 0
        for i in range(n):
            prevPlantTime += plants[i][0]
            seed_i_bloom_time = prevPlantTime + plants[i][1]
            maxTime = max(maxTime,seed_i_bloom_time)
        return maxTime 

if __name__ == '__main__':
	
	obj = Solution()

	plantTime = [1,2,3,2]

	growTime = [2,1,2,1]

	print(f'The Earliest time for all seeds to Bloom: {obj.earliestFullBloom(plantTime,growTime)}')