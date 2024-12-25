# LEETCODE - 1578
''' 
Given a string represent colors of ballons
we need to make sure that the rope with no adjacent same colors.
input = colors(string), neededTime(array)
	here, needTime[i] = time needed to remove ballon of colors[i]

output = MinTime to make the rope colorful ie. no adjacent same colors.


example :
Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.

example 2:
Let us now work on colors = 'aaaaba' timeNeeded = [1,2,1,4,2,3]

'''
class Solution:

	def solve(self,colors,timeNeeded):
		'''let arr = a a a a-> 1 2 1 4 : neededTime
		we compare 1st and 2nd, 
		we remove the smallest ie 1st , time += min(arr[0],arr[1])
		we compare 2nd and 3rd  we remove 3rd, time += min(arr[1],arr[2])
		we compare 2nd and 4th we remove 2nd, time += min(arr[1],arr[3])
		So, from the above illustration we can observe that not only the minTime value but also the maxTime has to be stored
		so, for every time colors[i-1]==colors[i],
		we take prevMaxTime = max(cur,prevMaxTime)
		and we keep on updating the prevMaxTime along as colors[i-1]==colors[i], else we set it to 0'''
		n = len(colors)
		time = 0
		prevMax = 0
		for i in range(n):
			if i>0 and colors[i-1]!=colors[i]:
				prevMax = 0
			cur = timeNeeded[i]
			time += min(prevMax,cur)
			prevMax = max(prevMax,cur)
		return time

if __name__ == '__main__':
 	
 	obj = Solution()

 	string = 'aaaaba'
 	timeNeeded = [1,2,1,4,2,3]

 	print(f'Time needed to make rope colorful : {obj.solve(string,timeNeeded)} ') 