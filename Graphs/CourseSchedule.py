# Course Schedule - Toposort : Leetcode-210

'''There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi before course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]
'''
from collections import defaultdict, deque

def findOrder(numCourses, prerequisites):
    # Step 1: Create the graph and in-degree array
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    # Step 2: Build the graph and fill in-degree array
    for course, prereq in prerequisites:
        graph[prereq].append(course)  # prereq -> course
        in_degree[course] += 1  # Increase in-degree for the course

    # Step 3: Initialize the queue with courses that have no prerequisites
    queue = deque()
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)

    # Step 4: Process the queue
    order = []
    while queue:
        current = queue.popleft()
        order.append(current)

        # Decrease the in-degree of neighboring courses
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 5: Check if we were able to take all courses
    if len(order) == numCourses:
        return order
    else:
        return []  # Cycle detected or not all courses can be completed

# Example usage
if __name__ == "__main__":
    print(findOrder(2, [[1, 0]]))  # Output: [0, 1]
    print(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # Output: [0, 1, 2, 3] or [0, 2, 1, 3]
    print(findOrder(1, []))  # Output: [0]