# Alien- Dictionary
'''
Given a sorted dictionary of an alien language having N words and k starting alphabets of a standard dictionary. 
Find the order of characters in the alien language.
in that dictorary words are there in a particular order which means dict[i] always comes before dict[i+1]

Example 1:
Input: N = 5, K = 4
dict = {"baa","abcd","abca","cab","cad"}
Output: b d a c
Explanation: 
We will analyze every consecutive pair to find out the order of the characters.
The pair “baa” and “abcd” suggests ‘b’ appears before ‘a’ in the alien dictionary.
The pair “abcd” and “abca” suggests ‘d’ appears before ‘a’ in the alien dictionary.
The pair “abca” and “cab” suggests ‘a’ appears before ‘c’ in the alien dictionary.
The pair “cab” and “cad” suggests ‘b’ appears before ‘d’ in the alien dictionary.
So, [‘b’, ‘d’, ‘a’, ‘c’] is a valid ordering.

Example 2:
Input: N = 3, K = 3
dict = {"caa","aaa","aab"}
Output: c a b
Explanation: Similarly, if we analyze the consecutive pair 
for this example, we will figure out [‘c’, ‘a’, ‘b’] is 
a valid ordering.
'''

''' 
Intution: 
step 1 : from the given list of words first find the adjacency list of characters
step 2 : Now use the Topological Sorting to find the order of character in the alien dictionary.
'''
from collections import defaultdict,deque
class Solution:

	def Topo(self,graph,in_degree):

		# add the characters whose indegree==0 to the Queue
		queue = deque()
		for i in in_degree:
			if in_degree[i]==0:
				queue.append(i)

		result = []
		while queue:
			char = queue.popleft()
			result.append(char)

			for nxt in graph[char]:
				in_degree[nxt]-=1
				if in_degree[nxt]==0:
					queue.append(nxt)
		return result

	def findOrder(self,wordList,n,k):

		# get the adjacency list
		graph = defaultdict(list)
		in_degree = {char : 0 for word in wordList for char in word}
		for i in range(n-1):
			s1 = wordList[i]
			s2 = wordList[i+1]
			mlen = min(len(s1),len(s2))
			ptr = 0
			while ptr<mlen:
				if s1[ptr]==s2[ptr]:
					ptr+=1
				else:
					graph[s1[ptr]].append(s2[ptr])
					in_degree[s2[ptr]] += 1
					break

		# print(graph)
		print(f"The indegree of vertices is : {in_degree}")

		# find the order with Toposort
		order = self.Topo(graph,in_degree)
		return order 

if __name__ == '__main__':
	
	dictionary = ["baa","abcd","abca","cab","cad"]
	N = 5
	K = 4

	obj = Solution()
	order = obj.findOrder(dictionary,N,K)
	print(f'The order of characters in Alien dictionary is : {order}')