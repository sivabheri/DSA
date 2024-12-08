
# Finding Largest and smallest elements
arr = [1,2,3,-1,4,2]
n = len(arr)

# to get largest element from an array
def largest(arr):
    mx = -1*float('inf')
    for i in range(n):
        mx = max(arr[i],mx)
    return mx
mx1 = largest(arr)
def seclarge(arr):
    mx = -1*float('inf')
    for i in range(n):
        if arr[i]!= largest(arr):
            mx = max(arr[i],mx)
    return mx
#print(seclarge(arr))

# Method 2

def ranges(arr):
    small = float('inf')
    s2 = float('inf')
    lrg = float('-inf')
    l2 = float('-inf')
    
    for i in range(n):
        small = min(small,arr[i])
        lrg = max(lrg,arr[i])
    for i in range(n):
        if arr[i]!=small:
            s2 = min(s2,arr[i])
        if arr[i]!=lrg:
            l2 = max(l2,arr[i])
    return lrg,l2,small,s2
large1 , large2 ,small1,small2 = ranges(arr)
'''print("large - 1 : {0}, large- 2 : {1}".format(large1,large2))
print("small - 1 : {0}, small-2 : {1}".format(small1,small2))
'''


 # Adding elements to map
#arr = [int(i) for i in input().split()]

n = len(arr)

def secLargest(arr):
    if n <2:
        return -1
    lgst = float('-inf')
    secLgst = float('-inf')
    for i in range(n):
        if (arr[i] > lgst):
            secLgst = lgst
            lgst = arr[i]
        elif (arr[i] > secLgst and arr[i] != lgst):
            secLgst = arr[i]
    return secLgst
    
ans = secLargest(arr)
#print(ans)

# MEthod 3


 # Adding elements to map
#arr = [int(i) for i in input().split()]
n = len(arr)

def secLargest(arr):
    
    lgst = float('-inf')
    secLgst = float('-inf')
    for i in range(n):
        if (arr[i] > lgst):
            secLgst = lgst
            lgst = arr[i]
        elif (arr[i] > secLgst and arr[i] != lgst):
            secLgst = arr[i]
    return secLgst
    
ans = secLargest(arr)
print(arr)
print(ans)