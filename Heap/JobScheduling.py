from typing import List

class Solution:
    # Greedy : TC = nlogn + n*max_deadline => nlogn
    def JobSequencing(self, id: List[int], deadline: List[int], profit: List[int]) -> List[int]:
        n = len(id)
        
        # Create a list of jobs as tuples (job_id, deadline, profit)
        jobs = [(id[i], deadline[i], profit[i]) for i in range(n)]
        
        # Sort the jobs based on profit in descending order
        jobs.sort(key=lambda x: x[2], reverse=True)
        
        # Find the maximum deadline
        max_deadline = max(deadline)
        
        # Initialize DP array
        dp = [0] * (max_deadline + 1)  # dp[t] stores max profit using t slots
        
        # Track the slots used
        slots = [-1] * (max_deadline + 1)  # -1 means the slot is unoccupied
        
        max_profit = 0
        jobs_done = 0
        
        # Iterate through the jobs
        for job_id, job_deadline, job_profit in jobs:
            # Check all possible slots for the job, from its deadline down to 1
            for t in range(min(max_deadline, job_deadline), 0, -1):
                if slots[t] == -1:  # If the slot is available
                    slots[t] = job_id  # Assign the job to this slot
                    dp[t] = max(dp[t], dp[t - 1] + job_profit)  # Update DP table
                    max_profit += job_profit
                    jobs_done += 1
                    break
        
        return [jobs_done, max_profit]

class Solution2:
    # using Heaps : TC = nlogn + nlogk = nlogn
    def jobScheduling(self, id: List[int], deadline: List[int], profit: List[int]) -> List[int]:
        # Create a list of jobs
        jobs = list(zip(id, deadline, profit))
        
        # Sort jobs based on profit in descending order
        jobs.sort(key=lambda x: x[2], reverse=True)
        
        # Max heap to keep track of the profits
        max_heap = []
        
        # Total profit and count of jobs
        total_profit = 0
        job_count = 0
        
        for job_id, job_deadline, job_profit in jobs:
            # If we can schedule the job within its deadline
            if job_count < job_deadline:
                heapq.heappush(max_heap, job_profit)
                total_profit += job_profit
                job_count += 1
            else:
                # If we can't schedule it, check if it's more profitable than the least profitable job
                if max_heap and max_heap[0] < job_profit:
                    total_profit += job_profit - heapq.heappop(max_heap)  # Replace the least profitable job
                    heapq.heappush(max_heap, job_profit)
        
        return [job_count, total_profit]

# Example usage
solution = Solution()
print(solution.JobSequencing([1, 2, 3, 4], [4, 1, 1, 1], [20, 10, 40, 30]))  # Output: [2, 60]
print(solution.JobSequencing([1, 2, 3, 4, 5], [2, 1, 2, 1, 1], [100, 19, 27, 25, 15]))  # Output: [2, 127]
print(solution.JobSequencing([1, 2, 3, 4], [3, 1, 2, 2], [50, 10, 20, 30]))  # Output: [3, 100]
