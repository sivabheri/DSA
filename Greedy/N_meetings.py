class Meetings:
	def __init__(self,start,end,pos):
		self.start = start
		self.end = end
		self.pos = pos

class Solution:

	def fun(self,s,e,n):
		arr = []
		for i in range(n):
			arr.append(Meetings(s[i], e[i], i))

		arr.sort(key = lambda x: x.end)#

		# To return the order in which the indices get executed
		ds = []
		ds.append(arr[0].pos)

		limit = arr[0].end
		cnt=1
		for i in range(1,n):
			if arr[i].start > limit:
				cnt+=1
				limit = arr[i].end
				ds.append(arr[i].pos)
		return cnt,ds,arr
if __name__=='__main__':

	ob = Solution()
	n = 6
	st = [1, 3, 0, 5, 8, 5]
	end = [2, 4, 5, 7, 9, 9]
	cnt , ds ,arr = ob.fun(st,end,n)
	print(cnt)
	print(ds)
	# print(arr[0].start)#