arr = [int(i) for i in input().split()]
n = len(arr)

mpp = {}

for i in range(n):
    ele = arr[i]
    if ele not in mpp:
        mpp[ele] = []
    mpp[ele].append(i)
        
print(mpp)
