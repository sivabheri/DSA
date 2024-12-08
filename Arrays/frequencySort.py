

# Sorting elements based on their frequencies
from collections import Counter
#from funtools import cmp_to_key

def count_sort(a, b, freq):
	if freq[a] != freq[b]:
		return freq[b] - freq[a]  # Sort by frequency (higher comes first)

	return a - b  # Sort by value (smaller comes first if frequency is the same)


class Solution:


	def freqSort(self,arr):

		n = len(arr)

		freq = Counter(arr)

		# def countSort(n):

		# 	# return (-freq[n],n)
		
		# using lambda fun
		arr.sort(key = lambda x:(-freq[x],x))
		#arr.sort(key = cmp_to_key(lambda a,b : count_sort(a,b,freq)))
		return arr

	def method2(self,arr):

		freq = Counter(arr)

		def fsort(num):
			return freq[num]

		new_arr = sorted(arr,key=fsort,reverse=True)

		return new_arr

if __name__ == '__main__':
	
	arr = [int(i) for i in input().strip('[]').split(',')]

	obj = Solution()

	print(obj.freqSort(arr))

	print(obj.method2(arr))