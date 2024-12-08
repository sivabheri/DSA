class Job:
	def __init__(self,Id,deadline,profit):
		self.Id = Id  
		self.deadline = deadline
		self.profit = profit

class Solution:

	def fun(self,ids,dl,pf,n):
		arr = []
		for i in range(n):
			arr.append(Job(ids[i],dl[i],pf[i]))#

		# To return the order in which the indices get executed
		

		arr.sort(key = lambda x: x.profit,reverse=True)#

		
		cnt = 0
		Tprofit = 0
		mxDeadline = max(dl)
		# for i in range(n):
		# 	mxDeadline = max(mxDeadline,arr[i].deadline)

		hashs = [-1]*(mxDeadline+1)

		'''
		for every job: i if hash[deadline:j] ==-1 # slot not assaigned so 
		hash[j] = Id, Once assaigned come out of loop J and assaign slots for remaining jobs
		mean while increment the count and add the profits that are assigned with slots.
		'''

		for i in range(n) :

			for j in range(arr[i].deadline,0,-1):

				if hashs[j]==-1:
					hashs[j] = arr[i].Id#
					cnt+=1
					Tprofit+= arr[i].profit
					break
				
		return cnt,Tprofit

if __name__=='__main__':

	ob = Solution()
	
	Id = [1,2,3,4]
	deadline = [4,1,2,2]
	profit = [20,10,40,30]#
	n = len(Id)
	cnt , TotalProfit = ob.fun(Id,deadline,profit,n)
	print(cnt)
	print(TotalProfit)
	# print(arr[0].start)#